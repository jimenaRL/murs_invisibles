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
        'country_filter_lang': 'fr',
        'year': {
            'minist_dossier.csv': 2010,
        }
    },
    "translator": {
        'country_lang': 'fr2fr',
        'indicator_lang': 'fr2fr',
    },
    "postprocesser": {
        'fns': {
            'minist_dossier.csv': 'perc',
        }
    },
}

Processer(config).process()
