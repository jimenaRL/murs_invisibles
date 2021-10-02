import os
from murs_invisibles import Processer

file_dir = os.path.dirname(os.path.realpath(__file__))
filter_indicator_path = os.path.join(file_dir, 'indicator_filter.txt')

config = {
    "base_path": os.path.dirname(os.path.realpath(__file__)),
    "origin_language": "fr",
    "merge": [
        {
            'name': 'insee_idf',
            'datas': [
                "INSEE-IDF - conseils municipaux_2021.csv",
                "INSEE-IDF - Part Femmes Cube & CSP Hauts de seine.csv",
            ],
            'sorter': "date_country"
        },
    ],
    "io": {
        "header": 0,
        "encoding": 'utf-8',
        'fns': {
            "INSEE-IDF - conseils municipaux_2021.csv": "one_save",
            "INSEE-IDF - Part Femmes Cube & CSP Hauts de seine.csv": "one_save",
        },
    },
    "preprocesser": {
        'fns': {
            "INSEE-IDF - conseils municipaux_2021.csv": ["virg2point"],
            "INSEE-IDF - Part Femmes Cube & CSP Hauts de seine.csv": ["remove_prop"],
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
            "INSEE-IDF - Part Femmes Cube & CSP Hauts de seine.csv": 2010,
        }
    },
    "mapper": {
        'fns': {
            "INSEE-IDF - conseils municipaux_2021.csv": "proportion100",
            "INSEE-IDF - Part Femmes Cube & CSP Hauts de seine.csv": "proportion100",
        }
    },
    "translator": {
    },
    "postprocesser": {
        'fns': {
            "INSEE-IDF - conseils municipaux_2021.csv": "perc",
            "INSEE-IDF - Part Femmes Cube & CSP Hauts de seine.csv": "perc",
        }
    },
    "sorter": {
        'fns': {
            "INSEE-IDF - conseils municipaux_2021.csv": "none",
            "INSEE-IDF - Part Femmes Cube & CSP Hauts de seine.csv": "none",
            "insee_idf": "none"
        }
    },
}

Processer(config).process()
