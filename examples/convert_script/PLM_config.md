# 预训练权重config
仅记录bert4torch需要另外配置的config
----
- bart/[FudanNLP_torch_base]
```json
{
  "attention_probs_dropout_prob": 0.1, 
  "hidden_act": "gelu", 
  "hidden_dropout_prob": 0.1, 
  "hidden_size": 768, 
  "initializer_range": 0.02, 
  "intermediate_size": 3072, 
  "max_position_embeddings": 512, 
  "num_attention_heads": 12, 
  "num_hidden_layers": 6, 
  "type_vocab_size": 2, 
  "vocab_size": 21128
}

```

- gpt/[thu-coai_torch_base]--CDial-GPT-LCCC-base
```json
{
  "attention_probs_dropout_prob": 0.1, 
  "directionality": "bidi", 
  "hidden_act": "gelu", 
  "hidden_dropout_prob": 0.1, 
  "hidden_size": 768, 
  "initializer_range": 0.02, 
  "intermediate_size": 3072, 
  "max_position_embeddings": 513, 
  "num_attention_heads": 12, 
  "num_hidden_layers": 12, 
  "vocab_size": 13088,
  "type_vocab_size": 3,
  "shared_segment_embeddings": true
}
```

- gpt2/[cpm_gpt2_torch]--cpm_lm_2.6b
```json
{
  "vocab_size": 30000,
  "hidden_size": 2560,
  "attention_probs_dropout_prob": 0.1,
  "hidden_dropout_prob": 0.1,
  "hidden_act": "gelu",
  "initializer_range": 0.014142135623731,
  "intermediate_size": 10240,
  "max_position_embeddings": 1024,
  "num_attention_heads": 32,
  "num_hidden_layers": 32
}
```

- gpt2/[gpt2-ml_torch_15g]
```json
{
  "vocab_size": 21130,
  "hidden_size": 1536,
  "attention_probs_dropout_prob": 0.1,
  "hidden_dropout_prob": 0.1,
  "hidden_act": "gelu",
  "initializer_range": 0.014142135623731,
  "intermediate_size": 6144,
  "max_position_embeddings": 1024,
  "num_attention_heads": 24,
  "num_hidden_layers": 48
}
```

- xlnet/[hit_torch_base]--chinese-xlnet-base
```json
{
  "architectures": [
    "XLNetLMHeadModel"
  ],
  "attn_type": "bi",
  "bi_data": false,
  "bos_token_id": 1,
  "clamp_len": -1,
  "intermediate_size": 3072,
  "hidden_size": 768,
  "hidden_dropout_prob": 0.1,
  "end_n_top": 5,
  "eos_token_id": 2,
  "hidden_act": "relu",
  "initializer_range": 0.02,
  "layer_norm_eps": 1e-12,
  "mem_len": null,
  "model_type": "xlnet",
  "num_attention_heads": 12,
  "num_hidden_layers": 12,
  "output_past": true,
  "pad_token_id": 5,
  "reuse_len": null,
  "same_length": false,
  "start_n_top": 5,
  "summary_activation": "tanh",
  "summary_last_hidden_dropout_prob": 0.1,
  "summary_type": "last",
  "summary_use_proj": true,
  "untie_r": true,
  "vocab_size": 32000
}
```

- t5/[google_mt5_torch_base]
```json
{
  "attention_probs_dropout_prob": 0.1, 
  "hidden_act": "gelu_new", 
  "hidden_dropout_prob": 0.1, 
  "hidden_size": 768, 
  "initializer_range": 0.02, 
  "intermediate_size": 2048, 
  "max_position_embeddings": 512, 
  "num_attention_heads": 12, 
  "num_hidden_layers": 12, 
  "type_vocab_size": 2, 
  "vocab_size": 250112,
  "relative_attention_num_buckets": 32
}
```

- t5/[uer_t5_torch_base]--t5-base-chinese-cluecorpussmall
```json
{
  "attention_probs_dropout_prob": 0.1, 
  "hidden_act": "relu", 
  "hidden_dropout_prob": 0.1, 
  "hidden_size": 768, 
  "initializer_range": 0.02, 
  "intermediate_size": 3072, 
  "max_position_embeddings": 512, 
  "num_attention_heads": 12, 
  "num_hidden_layers": 12, 
  "type_vocab_size": 2, 
  "vocab_size": 21228,
  "relative_attention_num_buckets": 32
}
```