import os
import json
import pandas as pd
from murs_invisibles import Processer

file_dir = os.path.dirname(os.path.realpath(__file__))
filter_indicator_path = os.path.join(file_dir, 'indicator_filter.txt')

config = {
    "base_path": os.path.dirname(os.path.realpath(__file__)),
    "origin_language": "fr",
    "io": {
        "header": 0,
        "encoding": 'utf-8',
        'fns': {
            "stop-violences - Violences au sein du couple et violences sexuelles 2018.csv": "one_save",
            "Etude nationale sur les morts violentes au sein du couple - 2014-2018.csv": "one_save",
        },
    },
    "preprocesser": {
        'fns': {
            "stop-violences - Violences au sein du couple et violences sexuelles 2018.csv": ["remove_prop"],
            "Etude nationale sur les morts violentes au sein du couple - 2014-2018.csv": ["remove_prop"],
        },
        'rename': {
            'country': 'pays',
            'year': 'annee',
            'indicator': 'nom',
            'value': 'valeur',
        },
    },
    "filter": {
        'filter_indicator_path': filter_indicator_path,
        'year': {
            "stop-violences - Violences au sein du couple et violences sexuelles 2018.csv": 2010,
            "Etude nationale sur les morts violentes au sein du couple - 2014-2018.csv": 2010,
        }
    },
    "mapper": {
        'fns': {
            "stop-violences - Violences au sein du couple et violences sexuelles 2018.csv": "proportion100",
            "Etude nationale sur les morts violentes au sein du couple - 2014-2018.csv": "proportion100",
        }
    },
    "translator": {
    },
    "postprocesser": {
        'fns': {
            "stop-violences - Violences au sein du couple et violences sexuelles 2018.csv": "perc",
            "Etude nationale sur les morts violentes au sein du couple - 2014-2018.csv": "perc",
        }
    },
    "sorter": {
        'fns': {
            "stop-violences - Violences au sein du couple et violences sexuelles 2018.csv": "none",
            "Etude nationale sur les morts violentes au sein du couple - 2014-2018.csv": "none",
        }
    },
}

Processer(config).process()
