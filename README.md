# pretrained doc2vec models on Japanese Wikipedia
This is a repository of doc2vec models trained on Japanese Wikipedia corpus.

## Pretrained models

- `dbow300d`
  - https://www.dropbox.com/s/j75s0eq4eeuyt5n/jawiki.doc2vec.dbow300d.tar.bz2?dl=0
  - Compressed file size: 5.48 GB
- `dmpv300d`
  - https://www.dropbox.com/s/njez3f1pjv9i9xj/jawiki.doc2vec.dmpv300d.tar.bz2?dl=0
  - Compressed file size: 8.86 GB


## Training setting
### Parameters

| param         | dbow300d | dmpv300d |
| :------------ | :------- | :------- |
| `dm`          | 0        | 1        |
| `vector_size` | 300      | 300      |
| `window`      | 15       | 10       |
| `alpha`       | 0.025    | 0.05     |
| `min_count`   | 5        | 2        |
| `sample`      | 1e-5     | 0        |
| `epochs`      | 20       | 20       |
| `dbow_words`  | 1        | 0        |

### Corpus

- [`jawiki-20190114-cirrussearch-content.json.gz`](https://dumps.wikimedia.org/other/cirrussearch/20190114/)

### Enviornments

- Tokenizer
  - MeCab: 0.996
  - NEologd: Periodic data update on 2019-01-17(Thu)
- requirements
  - gensim:3.7.0
  - numpy:1.16.0
