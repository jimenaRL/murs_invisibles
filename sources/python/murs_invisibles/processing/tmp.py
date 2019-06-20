#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
import json
from glob import glob

indicateor_fr2fr = "/Users/jimenarl/Desktop/git_murs/sources/python/murs_invisibles/processing/aux/translators/indicator_fr2fr.json"


folders = [
    "/Users/jimenarl/Desktop/git_murs/data/sources/CNC-Audiens/*/*.csv"
]

with open(indicateor_fr2fr, 'r', encoding='utf-8') as fp:
    country_dict = json.load(fp)
print(len(country_dict))


dicco = {}
for folder in folders:
    paths = glob(folder)
    for p in paths:
        df = pd.read_csv(p, encoding='utf-8')
        print(df.head())
        indicateurs = df.nom.tolist()
        dicco.update({i: i for i in indicateurs})

country_dict.update(dicco)
print(country_dict)

with open(indicateor_fr2fr, 'w',  encoding='utf-8') as fp:
    json.dump(country_dict,
        fp,
        indent=4)
