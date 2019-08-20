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
            'ENT4.csv': 'one_save',
            'GENDER_ENT1_01042019230825609_remove_ENT4.csv': 'sep_save',
        },
    },
    "preprocesser": {
        'fns': {
            'ENT4.csv': 'no_process',
            'GENDER_ENT1_01042019230825609_remove_ENT4.csv': 'diff_wm_insee',
        },
        'rename': {
            'country': 'Pays',
            'year': 'TIME',
            'indicator': 'Indicateur',
            'value': 'Value',
        },
    },
    "mapper": {
        'fns': {
            'ENT4.csv': 'proportion1',
            # TO DO: 'ecart100' or 'norm_wm' ?
            'GENDER_ENT1_01042019230825609_remove_ENT4.csv': 'ecart100',
        }
    },
    "filter": {
        'filter_indicator_path': filter_indicator_path,
        'country_filter_lang': 'fr',
        'year': {
            'ENT4.csv': 2015,
            'GENDER_ENT1_01042019230825609_remove_ENT4.csv': 2015,
        }
    },
    "translator": {
        'country_lang': 'fr2fr',
        'indicator_lang': 'fr2fr',
    },
    "postprocesser": {
        'fns': {
            'ENT4.csv': 'perc',
            'GENDER_ENT1_01042019230825609_remove_ENT4.csv': 'diff_perc',
        }
    },
    "sorter": {
        'fns': {
            'ENT4.csv': 'date_country',
            'GENDER_ENT1_01042019230825609_remove_ENT4.csv': 'date_country',
        }
    },
}

Processer(config).process()
