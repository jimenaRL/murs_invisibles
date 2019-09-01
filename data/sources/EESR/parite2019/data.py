import os
import json
import pandas as pd
from murs_invisibles import Processer


config = {
    "data_path": os.path.dirname(os.path.realpath(__file__)),
    "io": {
        "header": 0,
        "encoding": 'utf-8',
        "fns": {
            "parite2019_femmes-hommes.csv": "one_save",
            "parite2019_part_des_femmes.csv": "one_save",
        },
    },
    "preprocesser": {
        'fns': {
            "parite2019_femmes-hommes.csv": "diff_fh",
            "parite2019_part_des_femmes.csv": "no_process",

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
            "parite2019_femmes-hommes.csv": "ecart100",
            "parite2019_part_des_femmes.csv": "proportion100",
        }
    },
    "filter": {
        'filter_indicator_path': None,
        'country_filter_lang': 'fr',
        'year': {
            "parite2019_femmes-hommes.csv": 2010,
            "parite2019_part_des_femmes.csv": 2010,
        }
    },
    "translator": {
        'country_lang': 'fr2fr',
        'indicator_lang': 'fr2fr',
    },
    "postprocesser": {
        'fns': {
            "parite2019_femmes-hommes.csv": "diff_perc",
            "parite2019_part_des_femmes.csv": "perc",

        }
    },
    "sorter": {
        'fns': {
            "parite2019_femmes-hommes.csv": "none",
            "parite2019_part_des_femmes.csv": "none",
        }
    },
}

Processer(config).process()
