import os
import json
import pandas as pd
from murs_invisibles import Processer


config = {
    "data_path": os.path.dirname(os.path.realpath(__file__)),
    "io": {
        "header": 0,
        "encoding": 'utf-8',
        "fns": {
            "ecarts_salaires.csv": "one_save",
            "part de femmes.csv": "one_save",
            "hf.csv": "one_save",
        },
    },
    "preprocesser": {
        'fns': {
            "ecarts_salaires.csv": "remove_prop",
            "part de femmes.csv": "remove_prop",
            "hf.csv": "diff_fh",
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
            "ecarts_salaires.csv": "ecart100",
            "part de femmes.csv": "proportion100",
            "hf.csv": "ecart100",
        }
    },
    "filter": {
        'filter_indicator_path': None,
        'country_filter_lang': 'fr',
        'year': {
            "ecarts_salaires.csv": 2010,
            "part de femmes.csv": 2010,
            "hf.csv": 2010,
        }
    },
    "translator": {
        'country_lang': 'fr2fr',
        'indicator_lang': 'fr2fr',
    },
    "postprocesser": {
        'fns': {
            "ecarts_salaires.csv": "diff_perc",
            "part de femmes.csv": "perc",
            "hf.csv": "diff_perc",
        }
    },
    "sorter": {
        'fns': {
            "ecarts_salaires.csv": "none",
            "part de femmes.csv": "none",
            "hf.csv": "none",
        }
    },
}

Processer(config).process()
