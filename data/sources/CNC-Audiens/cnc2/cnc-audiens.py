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
            # "devis_moyen.csv": "",
            "part_films_nat.csv": "one_save",
            "part_films.csv": "one_save",
        },
    },
    "preprocesser": {
        'fns': {
            # "devis_moyen.csv": "",
            "part_films_nat.csv": ["no_process"],
            "part_films.csv": ["no_process"],
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
            # "devis_moyen.csv": "",
            "part_films_nat.csv": "proportion100",
            "part_films.csv": "proportion100",
        }
    },
    "filter": {
        'filter_indicator_path': None,
        'year': {
            "devis_moyen.csv": 2010,
            "part_films_nat.csv": 2010,
            "part_films.csv": 2010,
        }
    },
    "translator": {
    },
    "postprocesser": {
        'fns': {
            # "devis_moyen.csv": "",
            "part_films_nat.csv": "perc",
            "part_films.csv": "perc",
        }
    },
    "sorter": {
        'fns': {
            # "devis_moyen.csv": "",
            "part_films_nat.csv": "none",
            "part_films.csv": "none",
        }
    },
}

Processer(config).process()
