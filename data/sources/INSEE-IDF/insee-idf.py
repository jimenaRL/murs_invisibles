import os
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
            "INSEE-IDF - conseils municipaux_2021.csv": "one_save",
        },
    },
    "preprocesser": {
        'fns': {
            "INSEE-IDF - conseils municipaux_2021.csv": ["virg2point"],
        },
        'rename': {
            'country': ['pays'],
            'year': ['annee'],
            'indicator': ['nom'],
            'value': ['valeur'],
        },
    },
    "filter": {
        'filter_indicator_path': filter_indicator_path,
        'year': {
            "INSEE-IDF - conseils municipaux_2021.csv": 2010,
        }
    },
    "mapper": {
        'fns': {
            "INSEE-IDF - conseils municipaux_2021.csv": "proportion100",
        }
    },
    "translator": {
    },
    "postprocesser": {
        'fns': {
            "INSEE-IDF - conseils municipaux_2021.csv": "perc",

        }
    },
    "sorter": {
        'fns': {
            "INSEE-IDF - conseils municipaux_2021.csv": "none",
        }
    },
}

Processer(config).process()
