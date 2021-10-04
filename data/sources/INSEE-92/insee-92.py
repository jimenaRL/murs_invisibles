import os
from murs_invisibles import Processer

file_dir = os.path.dirname(os.path.realpath(__file__))
filter_indicator_path = os.path.join(file_dir, 'indicator_filter.txt')

config = {
    "base_path": os.path.dirname(os.path.realpath(__file__)),
    "origin_language": "fr",
    "merge": [
        {
            'name': 'insee_92',
            'tables': [
                "INSEE-92a - conseils municipaux_2021.csv",
                "INSEE-92a - Part Femmes Cube & CSP Hauts de seine.csv",
            ],
            'sorter': "date_country"
        },
    ],
    "io": {
        "header": 0,
        "encoding": 'utf-8',
        'fns': {
            "INSEE-92a - conseils municipaux_2021.csv": "one_save",
            "INSEE-92a - Part Femmes Cube & CSP Hauts de seine.csv": "one_save",
        },
    },
    "preprocesser": {
        'fns': {
            "INSEE-92a - conseils municipaux_2021.csv": ["virg2point"],
            "INSEE-92a - Part Femmes Cube & CSP Hauts de seine.csv": ["remove_prop"],
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
            "INSEE-92a - conseils municipaux_2021.csv": 2010,
            "INSEE-92a - Part Femmes Cube & CSP Hauts de seine.csv": 2010,
            "insee_92": 2010,
        }
    },
    "mapper": {
        'fns': {
            "INSEE-92a - conseils municipaux_2021.csv": "proportion100",
            "INSEE-92a - Part Femmes Cube & CSP Hauts de seine.csv": "proportion100",
        }
    },
    "translator": {
    },
    "postprocesser": {
        'fns': {
            "INSEE-92a - conseils municipaux_2021.csv": "perc",
            "INSEE-92a - Part Femmes Cube & CSP Hauts de seine.csv": "perc",
        }
    },
    "sorter": {
        'fns': {
            "INSEE-92a - conseils municipaux_2021.csv": "none",
            "INSEE-92a - Part Femmes Cube & CSP Hauts de seine.csv": "none",
            "insee_92": "none"
        }
    },
}

Processer(config).process()
