#! -*- coding: utf-8 -*-
# 预训练脚本，多GPU版版本

from bert4torch.models import build_transformer_model
from bert4torch.snippets import sequence_padding, Callback
from torch.utils.data import Dataset
import torch.nn as nn
import torch
import torch.optim as optim
from torch.utils.data import DataLoader
import json
import os
import shelve
import random


# 语料路径和模型保存路径
model_saved_path = './bert_model.ckpt'
corpus_dir = 'E:/Github/bert4torch/examples/datasets/pretrain'

# 其他配置
maxlen = 512
batch_size = 4096
config_path = 'F:/Projects/pretrain_ckpt/bert/[google_tf_base]--chinese_L-12_H-768_A-12/bert_config.json'
checkpoint_path = 'F:/Projects/pretrain_ckpt/bert/[google_tf_base]--chinese_L-12_H-768_A-12/pytorch_model.bin'  # 如果从零训练，就设为None
learning_rate = 0.00176
weight_decay_rate = 0.01  # 权重衰减
num_warmup_steps = 3125
num_train_steps = 125000
steps_per_epoch = 10000
grad_accum_steps = 16  # 大于1即表明使用梯度累积
epochs = num_train_steps * grad_accum_steps // steps_per_epoch
exclude_from_layer_adaptation = ['Norm', 'bias']
device = 'cuda' if torch.cuda.is_available() else 'cpu'


# 读取数据集，构建数据张量
class MyDataset(Dataset):
    def __init__(self, file):
        super(MyDataset, self).__init__()
        self.file = file
        self.len = self._get_dataset_length()
        self.db = self._load_data()

    def __getitem__(self, index):
        return self.db[str(index)]

    def __len__(self):
        return self.len

    def _get_dataset_length(self):
        file_record_info = self.file + ".json"
        record_info = json.load(open(file_record_info, "r", encoding="utf-8"))
        return record_info["samples_num"]

    def _load_data(self):
        return shelve.open(self.file)

def collate_fn(batch):
    batch_token_ids, batch_labels = [], []
    for item in batch:
        batch_token_ids.append(item['input_ids'])
        batch_labels.append(item['masked_lm_labels'])

    batch_token_ids = torch.tensor(sequence_padding(batch_token_ids), dtype=torch.long, device=device)
    batch_labels = torch.tensor(batch_labels, dtype=torch.long, device=device)
    return [batch_token_ids], batch_labels


# 从语料文件夹中随机选取一个文件，生成dataloader
def get_train_dataloader():
    files = os.listdir(corpus_dir)
    sel_file = os.path.join(corpus_dir, random.choice(files))
    train_dataloader = DataLoader(MyDataset(sel_file), batch_size=batch_size, shuffle=True, collate_fn=collate_fn)
    os.remove(sel_file)
    return train_dataloader
train_dataloader = get_train_dataloader()

model = build_transformer_model(config_path, checkpoint_path, segment_vocab_size=0, with_mlm='linear').to(device)

# weight decay
param_optimizer = list(model.named_parameters())
no_decay = ['bias', 'LayerNorm.bias', 'LayerNorm.weight']
optimizer_grouped_parameters = [
    {'params': [p for n, p in param_optimizer if not any(nd in n for nd in no_decay)], 'weight_decay': weight_decay_rate},
    {'params': [p for n, p in param_optimizer if any(nd in n for nd in no_decay)], 'weight_decay': 0.0}
]

# 定义使用的loss和optimizer，这里支持自定义
model.compile(
    loss=nn.CrossEntropyLoss(ignore_index=0),
    optimizer=optim.Adam(optimizer_grouped_parameters, lr=2e-5, weight_decay=weight_decay_rate)
)


class ModelCheckpoint(Callback):
    """自动保存最新模型
    """
    def on_dataloader_end(self, logs=None):
        model.train_dataloader = get_train_dataloader() # 重新生成dataloader

    def on_epoch_end(self, global_step, epoch, logs=None):
        model.save_weights(model_saved_path)

if __name__ == '__main__':
    # 保存模型
    checkpoint = ModelCheckpoint()

    # 模型训练
    model.fit(
        train_dataloader,
        steps_per_epoch=steps_per_epoch,
        grad_accumulation_steps=grad_accum_steps,
        epochs=epochs,
        callbacks=[checkpoint],
    )