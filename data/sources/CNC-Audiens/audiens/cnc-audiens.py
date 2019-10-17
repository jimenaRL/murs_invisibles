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
            "emploi_spect_vivant_cat_so.csv": "one_save",
            "emploi_spect_vivant.csv": "one_save",
            "intermitants.csv": "one_save",
        },
    },
    "preprocesser": {
        'fns': {
            "emploi_spect_vivant_cat_so.csv": "no_process",
            "emploi_spect_vivant.csv": "no_process",
            "intermitants.csv": "virg2point",
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
            "emploi_spect_vivant_cat_so.csv": "proportion100",
            "emploi_spect_vivant.csv": "proportion100",
            "intermitants.csv": "proportion100",
        }
    },
    "filter": {
        'filter_indicator_path': None,
        'year': {
            "emploi_spect_vivant_cat_so.csv": 2010,
            "emploi_spect_vivant.csv": 2010,
            "intermitants.csv": 2010,
        }
    },
    "translator": {
    },
    "postprocesser": {
        'fns': {
            "emploi_spect_vivant_cat_so.csv": "diff_perc",
            "emploi_spect_vivant.csv": "perc",
            "intermitants.csv": "perc",
        }
    },
    "sorter": {
        'fns': {
            "emploi_spect_vivant_cat_so.csv": "none",
            "emploi_spect_vivant.csv": "none",
            "intermitants.csv": "none",
        }
    },
}

Processer(config).process()
