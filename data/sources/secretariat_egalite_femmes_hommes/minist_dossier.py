import os
import json
import pandas as pd
from murs_invisibles import Processer

file_dir = os.path.dirname(os.path.realpath(__file__))
filter_indicator_path = os.path.join(file_dir, 'indicator_filter.txt')

config = {
    "base_path": file_dir,
    "origin_language": "fr",
    "target_language": "fr",
    "io": {
        "header": 0,
        "encoding": 'utf-8',
        "fns": {
            'minist_dossier.csv': 'one_save',
        },
    },
    "preprocesser": {
        'fns': {
            'minist_dossier.csv': 'remove_prop',
        },
        'rename': {
            'country': 'pays',
            'year': 'annee',
            'indicator': 'formulation',
            'value': 'value'
        },
    },
    "mapper": {
        'fns': {
            'minist_dossier.csv': 'proportion100',
        }
    },
    "filter": {
        'filter_indicator_path': filter_indicator_path,
        'year': {
            'minist_dossier.csv': 2010,
        }
    },
    "translator": {
    },
    "postprocesser": {
        'fns': {
            'minist_dossier.csv': 'perc',
        }
    },
    "sorter": {
        'fns': {
            'minist_dossier.csv': 'none',
        }
    },
}

Processer(config).process()
