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
            "apprentis.csv": "one_save",
            "personnel.csv": "one_save",
            "r&d.csv": "one_save",
        },
    },
    "preprocesser": {
        'fns': {
            "apprentis.csv": "virg2point",
            "personnel.csv": "virg2point",
            "r&d.csv": "virg2point",
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
            "apprentis.csv": "ecart100",
            "personnel.csv": "ecart100",
            "r&d.csv": "ecart100",
        }
    },
    "filter": {
        'filter_indicator_path': None,
        'country_filter_lang': 'fr',
        'year': {
            "apprentis.csv": 2010,
            "personnel.csv": 2010,
            "r&d.csv": 2010,
        }
    },
    "translator": {
        'country_lang': 'fr2fr',
        'indicator_lang': 'fr2fr',
    },
    "postprocesser": {
        'fns': {
            "apprentis.csv": "perc",
            "personnel.csv": "perc",
            "r&d.csv": "perc",
        }
    },
}

Processer(config).process()
