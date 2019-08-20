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
            'GENDER_EDU_29102017131322363.csv': 'sep_save',
        },
    },
    "preprocesser": {
        'fns': {
            'GENDER_EDU_29102017131322363.csv': 'diff_wm_insee',
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
            'GENDER_EDU_29102017131322363.csv': 'ecart100',
        }
    },
    "filter": {
        'filter_indicator_path': None,
        'country_filter_lang': 'fr',
        'year': {
            'GENDER_EDU_29102017131322363.csv': 2010,
        }
    },
    "translator": {
        'country_lang': 'fr2fr',
        'indicator_lang': 'en2fr',
    },
    "postprocesser": {
        'fns': {
            'GENDER_EDU_29102017131322363.csv': 'diff_perc',
        }
    },
    "sorter": {
        'fns': {
            'GENDER_EDU_29102017131322363.csv': 'date_country',
        }
    },
}

Processer(config).process()
