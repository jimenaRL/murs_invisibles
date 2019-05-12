import os
import json
import pandas as pd
from murs_invisibles import Processer


file_dir = os.path.dirname(os.path.realpath(__file__))
filter_indicator_path = os.path.join(file_dir, 'indicator_filter.txt')

config = {
    "data_path": os.path.dirname(os.path.realpath(__file__)),
    "io": {
        "header": 0,
        "encoding": 'utf-8',
        "fns": {
            'GOV_2017_03042019165415175.csv': 'sep_save',
        },
    },
    "preprocesser": {
        'fns': {
            'GOV_2017_03042019165415175.csv': 'no_process',
        },
        'rename': {
            'country': 'Country',
            'year': 'Year',
            'indicator': 'Indicator',
            'value': 'Value',
        },
    },
    "mapper": {
        'fns': {
            'GOV_2017_03042019165415175.csv': 'proportion100',
        }
    },
    "filter": {
        'filter_indicator_path': filter_indicator_path,
        'country_filter_lang': 'en',
        'year': {
            'GOV_2017_03042019165415175.csv': 2010,
        }
    },
    "translator": {
        'country_lang': 'en2fr',
        'indicator_lang': 'en2fr',
    },
    "postprocesser": {
        'fns': {
            'GOV_2017_03042019165415175.csv': 'perc',
        }
    },
}

Processer(config).process()
