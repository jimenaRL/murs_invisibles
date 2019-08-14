import os
import json
import pandas as pd
from murs_invisibles import Processer

config = {
    "data_path": os.path.dirname(os.path.realpath(__file__)),
    "io": {
        "header": 1,
        "encoding": 'latin1',
        "fns": {
            'SYB61_T05_Seats held by Women in Parliament.csv': 'one_save',
            'SYB61_T06_Ratio of Girls to Boys in Education.csv': 'one_save',
        },
    },
    "preprocesser": {
        'fns': {
            'SYB61_T05_Seats held by Women in Parliament.csv': 'no_process',
            # /!\ problem with ’ character /!\ #
            'SYB61_T06_Ratio of Girls to Boys in Education.csv': 'no_process',
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
        'country_filter_lang': 'en',
        'year': {
            'SYB61_T05_Seats held by Women in Parliament.csv': 2010,
            'SYB61_T06_Ratio of Girls to Boys in Education.csv': 2010
        }
    },
    "translator": {
        'country_lang': 'en2fr',
        'indicator_lang': 'en2fr',
    },
    "postprocesser": {
        'fns': {
            'SYB61_T05_Seats held by Women in Parliament.csv': 'perc',
            'SYB61_T06_Ratio of Girls to Boys in Education.csv': 'ratio',
        }
    },
}

Processer(config).process()
