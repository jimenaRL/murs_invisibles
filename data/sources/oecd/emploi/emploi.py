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
            'GENDER_EMP_01042019231318532.csv': 'sep_save',
        },
    },
    "preprocesser": {
        'fns': {
            'GENDER_EMP_01042019231318532.csv': 'diff_wm',
        },
        'rename': {
            'country': 'Pays',
            'year': 'TIME',
            'indicator': 'Indicateur',
            'value': 'Value'
        },
    },
    "mapper": {
        'fns': {
            'GENDER_EMP_01042019231318532.csv': 'ecart100',
        }
    },
    "filter": {
        'filter_indicator_path': filter_indicator_path,
        'country_filter_lang': 'fr',
        'year': {
            'GENDER_EMP_01042019231318532.csv': 2016,
        }
    },
    "translator": {
        'country_lang': 'fr2fr',
        'indicator_lang': 'fr2fr',
    },
    "postprocesser": {
        'fns': {
           'GENDER_EMP_01042019231318532.csv': 'diff_perc',  # ?????
        }
    },
    "sorter": {
        'fns': {
            'GENDER_EMP_01042019231318532.csv': 'date_country',
        }
    },
}

Processer(config).process()
