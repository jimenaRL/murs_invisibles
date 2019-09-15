import os
import json
import pandas as pd
from murs_invisibles import Processer


config = {
    "base_path": os.path.dirname(os.path.realpath(__file__)),
    "origin_language": "fr",
    "target_language": "es",
    "io": {
        "header": 0,
        "encoding": 'utf-8',
        "fns": {
            "all.csv": "one_save",
        },
    },
    "preprocesser": {
        'fns': {
            "all.csv": "virg2point",
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
            "all.csv": "diffFH_100",
        }
    },
    "filter": {
        'filter_indicator_path': None,
        'year': {
            "all.csv": 2010,
        }
    },
    "translator": {
    },
    "postprocesser": {
        'fns': {
            "all.csv": "perc",
        }
    },
    "sorter": {
        'fns': {
            "all.csv": "none",
        }
    },
}

Processer(config).process()
