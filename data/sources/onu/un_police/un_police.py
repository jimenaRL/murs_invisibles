import os
import json
import pandas as pd
from murs_invisibles import Processer

config = {
    "base_path": os.path.dirname(os.path.realpath(__file__)),
    "origin_language": "en",
    "merge": {
        'Share_of_female_police_officers': [
            'Share_of_female_police_officers-TREATED.csv',
            'cjs_police_table_Full_Data_data-TREATED.csv',
            '46 - Share of female police officers_data.csv'
        ]
    },
    "io": {
        "header": 0,
        "encoding": 'latin1',
        "fns": {
            'Share_of_female_police_officers-TREATED.csv': 'none',
            'cjs_police_table_Full_Data_data-TREATED.csv': 'none',
            '46 - Share of female police officers_data.csv': 'none',

        },
    },
    "preprocesser": {
        'fns': {
            'cjs_police_table_Full_Data_data-TREATED.csv': ['no_process'],
            'Share_of_female_police_officers-TREATED.csv': ['no_process'],
            '46 - Share of female police officers_data.csv': ['no_process'],
        },
        'rename': {
            'country': ['country'],
            'year': ['year'],
            'indicator': ['indicator'],
            'value': ['value']
        },
    },
    "mapper": {
        'fns': {
            'cjs_police_table_Full_Data_data-TREATED.csv': 'proportion100',
            'Share_of_female_police_officers-TREATED.csv': 'proportion100',
            '46 - Share of female police officers_data.csv': 'proportion1',
        }
    },
    "filter": {
        'filter_indicator_path': None,
        'year': {
            'cjs_police_table_Full_Data_data-TREATED.csv': 2012,
            'Share_of_female_police_officers-TREATED.csv': 2012,
            '46 - Share of female police officers_data.csv': 2015,
        }
    },
    "translator": {
    },
    "postprocesser": {
        'fns': {
            'cjs_police_table_Full_Data_data-TREATED.csv': 'perc',
            'Share_of_female_police_officers-TREATED.csv': 'perc',
            '46 - Share of female police officers_data.csv': 'percX100',
        }
    },
    "sorter": {
        'fns': {
            'cjs_police_table_Full_Data_data-TREATED.csv': 'date_country',
            'Share_of_female_police_officers-TREATED.csv': 'date_country',
            '46 - Share of female police officers_data.csv': 'none',
        }
    },
}

Processer(config).process()
