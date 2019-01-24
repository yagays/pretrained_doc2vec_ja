import bz2
import gzip
import json
import pickle

import MeCab
from tqdm import tqdm


wakati = MeCab.Tagger("-O wakati -d /usr/local/lib/mecab/dic/mecab-ipadic-neologd")
wakati.parse("")

cirrus_all = {}
with gzip.open("data/jawiki-20190114-cirrussearch-content.json.gz") as fin:
    with bz2.open("data/20190114cirrus_all.tsv.bz2", 'wt') as fout:
        for line in tqdm(fin, total=2271620):
            json_line = json.loads(line)
            if "index" not in json_line:
                title = json_line["title"]
                text = json_line["text"]

                if title and text:
                    print("\t".join([title, wakati.parse(text).strip()]), file=fout)
