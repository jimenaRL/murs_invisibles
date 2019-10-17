import os
import json
import pandas as pd
from murs_invisibles import Processer


config = {
    "base_path": os.path.dirname(os.path.realpath(__file__)),
    "origin_language": "fr",
    "io": {
        "header": 0,
        "encoding": 'utf-8',
        "fns": {
            "ecarts_salaires.csv": "one_save",
            "part de femmes.csv": "one_save"
        },
    },
    "preprocesser": {
        'fns': {
            "ecarts_salaires.csv": "remove_prop",
            "part de femmes.csv": "remove_prop"
        },
        'rename': {
            'country': 'pays',
            'year': 'annee',
            'indicator': 'nom',
            'value': 'part de femmes',
        },
    },
    "mapper": {
        'fns': {
            "ecarts_salaires.csv": "diffFH_100",
            "part de femmes.csv": "proportion100"
        }
    },
    "filter": {
        'filter_indicator_path': None,
        'year': {
            "ecarts_salaires.csv": 2010,
            "part de femmes.csv": 2010,
            "hf.csv": 2010,
        }
    },
    "translator": {
    },
    "postprocesser": {
        'fns': {
            "ecarts_salaires.csv": "diff_perc",
            "part de femmes.csv": "perc"
        }
    },
    "sorter": {
        'fns': {
            "ecarts_salaires.csv": "none",
            "part de femmes.csv": "none"
        }
    },
}

Processer(config).process()
