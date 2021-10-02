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
            "secret - écart salaire hommes et femmes.csv": "one_save",
            "secret - part de femmes.csv": "split3"
        },
    },
    "preprocesser": {
        'fns': {
            "secret - écart salaire hommes et femmes.csv": ["remove_prop"],
            "secret - part de femmes.csv": ["remove_prop"]
        },
        'rename': {
            'country': ['pays'],
            'year': ['annee'],
            'indicator': ['nom'],
            'value': ['part de femmes', 'écart salaire hommes et femmes'],
        },
    },
    "mapper": {
        'fns': {
            "secret - écart salaire hommes et femmes.csv": "diffFH_100",
            "secret - part de femmes.csv": "proportion100"
        }
    },
    "filter": {
        'filter_indicator_path': None,
        'year': {
            "secret - écart salaire hommes et femmes.csv": 2010,
            "secret - part de femmes.csv": 2010,
            "hf.csv": 2010,
        }
    },
    "translator": {
    },
    "postprocesser": {
        'fns': {
            "secret - écart salaire hommes et femmes.csv": "diff_perc",
            "secret - part de femmes.csv": "perc"
        }
    },
    "sorter": {
        'fns': {
            "secret - écart salaire hommes et femmes.csv": "none",
            "secret - part de femmes.csv": "none"
        }
    },
}

Processer(config).process()
