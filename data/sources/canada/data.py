import os
import json
import pandas as pd
from murs_invisibles import Processer

file_dir = os.path.dirname(os.path.realpath(__file__))
filter_indicator_path = os.path.join(file_dir, 'indicator_filter.txt')

config = {
    "data_path": file_dir,
    "io": {
        "header": 0,
        "encoding": 'utf-8',
        "fns": {
            "taux.csv": "one_save",
            "revenu_moyens.csv": "one_save",
            "culture.csv": "one_save",
        },
    },
    "preprocesser": {
        'fns': {
            "revenu_moyens.csv": "remove_dollar_and_k_diff_money",
            "culture.csv": "no_process",
            "taux.csv": "diff_fh",
        },
        'rename': {
            'country': 'pays',
            'year': 'annee',
            'indicator': 'nom',
            'value': 'part de femmes',
        },
    },
    "mapper": {
        'fns': {
            "culture.csv": "proportion100",
            "taux.csv": "ecart100",
            "revenu_moyens.csv": "women2men_ratio",
        }
    },
    "filter": {
        'filter_indicator_path': filter_indicator_path,
        'country_filter_lang': 'fr',
        'year': {
            "culture.csv": 2006,
            "taux.csv": 2006,
            "revenu_moyens.csv": 2006,
        }
    },
    "translator": {
        'country_lang': 'fr2fr',
        'indicator_lang': 'fr2fr',
    },
    "postprocesser": {
        'fns': {
            "culture.csv": "perc",
            "taux.csv": "diff_perc",
            "revenu_moyens.csv": "diff_money",
        }
    },
}

Processer(config).process()
