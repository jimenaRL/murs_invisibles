import os
import json
import pandas as pd
from murs_invisibles import Processer

file_dir = os.path.dirname(os.path.realpath(__file__))
filter_indicator_path = os.path.join(file_dir, 'indicator_filter.txt')

config = {
    "base_path": file_dir,
    "origin_language": "fr",
    "merge": {
        'ENT4_GIDDB2019_poste_de_direction': [
            'ENT4.csv',
            'GIDDB2019_poste_de_direction.csv',
        ]
    },
    "io": {
        "header": 0,
        "encoding": 'utf-8',
        "fns": {
            'ENT4.csv': 'one_save',
           # 'GENDER_ENT1_01042019230825609_remove_ENT4.csv': 'sep_save',
            'GIDDB2019_poste_de_direction.csv': 'one_save',
        },
    },
    "preprocesser": {
        'fns': {
            'ENT4.csv': ['no_process'],
            'GENDER_ENT1_01042019230825609_remove_ENT4.csv': [
                'get_wm_oecd',
                'percRel100'
            ],
            'GIDDB2019_poste_de_direction.csv': ['no_process'],
        },
        'rename': {
            'country': ['Pays'],
            'year': ['TIME'],
            'indicator': ['VAR', 'Indicateur'],
            'value': ['Value'],
        },
    },
    "mapper": {
        'fns': {
            'ENT4.csv': 'proportion100',
            'GENDER_ENT1_01042019230825609_remove_ENT4.csv': 'diffFH_100',
            'GIDDB2019_poste_de_direction.csv': 'proportion1',
        }
    },
    "filter": {
        'filter_indicator_path': filter_indicator_path,
        'year': {
            'ENT4.csv': 2015,
            'GENDER_ENT1_01042019230825609_remove_ENT4.csv': 2015,
            'GIDDB2019_poste_de_direction.csv': 2010,
        }
    },
    "translator": {
    },
    "postprocesser": {
        'fns': {
            'ENT4.csv': 'perc',
            'GENDER_ENT1_01042019230825609_remove_ENT4.csv': 'diff_perc',
            'GIDDB2019_poste_de_direction.csv': 'percX100',
        }
    },
    "sorter": {
        'fns': {
            'ENT4.csv': 'date_country',
            'GENDER_ENT1_01042019230825609_remove_ENT4.csv': 'date_country',
            'GIDDB2019_poste_de_direction.csv': 'date_country',
        }
    },
}

Processer(config).process()
