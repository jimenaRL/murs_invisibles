import os
import json
import pandas as pd
from murs_invisibles import Processer

file_dir = os.path.dirname(os.path.realpath(__file__))
filter_indicator_path = os.path.join(file_dir, 'indicator_filter.txt')

config = {
    "base_path": file_dir,
    "origin_language": "es",
    "target_language": "es",
    "io": {
        "header": 0,
        "encoding": 'utf-8',
        "fns": {
            "taux.csv": "one_save",
            "revenu_moyens.csv": "one_save",
            "culture.csv": "one_save",
            "effectif_professions_culture_communications.csv": "one_save",
        },
    },
    "preprocesser": {
        'fns': {
            "revenu_moyens.csv": "remove_dollar_and_k_diff_insee",
            "culture.csv": "no_process",
            "taux.csv": "diff_fh",
            "effectif_professions_culture_communications.csv": "perc_fsurtotal",
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
            "culture.csv": "proportion100",
            "taux.csv": "ecart100",
            "revenu_moyens.csv": "ecart100",
            "effectif_professions_culture_communications.csv": "proportion100",
        }
    },
    "filter": {
        'filter_indicator_path': filter_indicator_path,
        'year': {
            "culture.csv": 2006,
            "taux.csv": 2006,
            "revenu_moyens.csv": 2006,
            "effectif_professions_culture_communications.csv": 2006,
        }
    },
    "translator": {
    },
    "postprocesser": {
        'fns': {
            "culture.csv": "perc",
            "taux.csv": "diff_perc",
            "revenu_moyens.csv": "diff_perc",
            "effectif_professions_culture_communications.csv": "perc",
        }
    },
    "sorter": {
        'fns': {
            "taux.csv": "none",
            "revenu_moyens.csv": "none",
            "culture.csv": "none",
            "effectif_professions_culture_communications.csv": "none",
        }
    },
}

Processer(config).process()
