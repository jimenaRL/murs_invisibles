import os
import json
import pandas as pd
from murs_invisibles import Processer

config = {
    "base_path": os.path.dirname(os.path.realpath(__file__)),
    "origin_language": "en",
    "io": {
        "header": 1,
        "encoding": 'latin1',
        "fns": {
            'SYB61_T05_Seats held by Women in Parliament.csv': 'split4',
            'SYB61_T06_Ratio of Girls to Boys in Education.csv': 'split4',
        },
    },
    "preprocesser": {
        'fns': {
            'SYB61_T05_Seats held by Women in Parliament.csv': ['no_process'],
            # /!\ problem with ’ character /!\ #
            'SYB61_T06_Ratio of Girls to Boys in Education.csv': ['no_process'],
        },
        'rename': {
            'country': 'Unnamed: 1',
            'year': 'Year',
            'indicator': 'Series',
            'value': 'Value'
        },
    },
    "mapper": {
        'fns': {
            'SYB61_T05_Seats held by Women in Parliament.csv': 'proportion100',
            'SYB61_T06_Ratio of Girls to Boys in Education.csv': 'women2men_ratio'
        }
    },
    "filter": {
        'filter_indicator_path': None,
        'year': {
            'SYB61_T05_Seats held by Women in Parliament.csv': 2012,
            'SYB61_T06_Ratio of Girls to Boys in Education.csv': 2012
        }
    },
    "translator": {
    },
    "postprocesser": {
        'fns': {
            'SYB61_T05_Seats held by Women in Parliament.csv': 'perc',
            'SYB61_T06_Ratio of Girls to Boys in Education.csv': 'women2men_ratio',
        }
    },
    "sorter": {
        'fns': {
            'SYB61_T05_Seats held by Women in Parliament.csv': 'date_country',
            'SYB61_T06_Ratio of Girls to Boys in Education.csv': 'date_country',
        }
    },
}

Processer(config).process()
