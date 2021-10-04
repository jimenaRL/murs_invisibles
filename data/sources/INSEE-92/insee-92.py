import os
from murs_invisibles import Processer

file_dir = os.path.dirname(os.path.realpath(__file__))
filter_indicator_path = os.path.join(file_dir, 'indicator_filter.txt')

config = {
    "base_path": os.path.dirname(os.path.realpath(__file__)),
    "origin_language": "fr",
    "merge": [
        {
            'name': 'insee_92a',
            'tables': [
                "INSEE-92a - conseils municipaux_2021.csv",
                "INSEE-92a - Part Femmes Cube & CSP Hauts de seine.csv",
            ],
            'sorter': "date_country"
        },
        {
            'name': 'insee_92b-ecarts-taux',
            'tables': [
                "INSEE-92b - Ecart taux diplomes Hauts de seine.csv",
                "INSEE-92b - ECARTS Taux Hauts de seine.csv",
            ],
            'sorter': "date_country"
        },
        {
            'name': 'insee_92b-ecarts-salaires',
            'tables': [
                "INSEE-92b - Ecarts Salaires 2019- Villes Haut de Seine.csv",
                "INSEE-92b - ECARTS Salaires Hauts de seine.csv",
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
            "INSEE-92b - Ecart taux diplomes Hauts de seine.csv": "one_save",
            "INSEE-92b - ECARTS Taux Hauts de seine.csv": "one_save",
            "INSEE-92b - Ecarts Salaires 2019- Villes Haut de Seine.csv": "one_save",
            "INSEE-92b - ECARTS Salaires Hauts de seine.csv": "one_save",
        },
    },
    "preprocesser": {
        'fns': {
            "INSEE-92a - conseils municipaux_2021.csv": ["virg2point"],
            "INSEE-92a - Part Femmes Cube & CSP Hauts de seine.csv": ["remove_prop"],
            "INSEE-92b - Ecart taux diplomes Hauts de seine.csv": [],
            "INSEE-92b - ECARTS Taux Hauts de seine.csv": [],
            "INSEE-92b - Ecarts Salaires 2019- Villes Haut de Seine.csv": [],
            "INSEE-92b - ECARTS Salaires Hauts de seine.csv": [],
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
            "INSEE-92b - Ecart taux diplomes Hauts de seine.csv": 2010,
            "INSEE-92b - ECARTS Taux Hauts de seine.csv": 2010,
            "INSEE-92b - Ecarts Salaires 2019- Villes Haut de Seine.csv": 2010,
            "INSEE-92b - ECARTS Salaires Hauts de seine.csv": 2010,
            "insee_92a": 2010,
            "insee_92b-ecarts-taux": 2010,
            "insee_92b-ecarts-salaires": 2010
        }
    },
    "mapper": {
        'fns': {
            "INSEE-92a - conseils municipaux_2021.csv": "proportion100",
            "INSEE-92a - Part Femmes Cube & CSP Hauts de seine.csv": "proportion100",
            "INSEE-92b - Ecart taux diplomes Hauts de seine.csv": "diffFH_10",
            "INSEE-92b - ECARTS Taux Hauts de seine.csv": "diffFH_10",
            "INSEE-92b - Ecarts Salaires 2019- Villes Haut de Seine.csv": "proportion100",
            "INSEE-92b - ECARTS Salaires Hauts de seine.csv": "proportion100",
        }
    },
    "translator": {
    },
    "postprocesser": {
        'fns': {
            "INSEE-92a - conseils municipaux_2021.csv": "perc",
            "INSEE-92a - Part Femmes Cube & CSP Hauts de seine.csv": "perc",
            "INSEE-92b - Ecart taux diplomes Hauts de seine.csv": "diff_pp",
            "INSEE-92b - ECARTS Taux Hauts de seine.csv": "diff_pp",
            "INSEE-92b - Ecarts Salaires 2019- Villes Haut de Seine.csv": "diff_perc",
            "INSEE-92b - ECARTS Salaires Hauts de seine.csv": "diff_perc",
        }
    },
    "sorter": {
        'fns': {
            "INSEE-92a - conseils municipaux_2021.csv": "none",
            "INSEE-92a - Part Femmes Cube & CSP Hauts de seine.csv": "none",
            "INSEE-92b - Ecart taux diplomes Hauts de seine.csv": "none",
            "INSEE-92b - ECARTS Taux Hauts de seine.csv": "none",
            "INSEE-92b - Ecarts Salaires 2019- Villes Haut de Seine.csv": "none",
            "INSEE-92b - ECARTS Salaires Hauts de seine.csv": "none",
            "insee_92a": "none",
            "insee_92b-ecarts-taux": "none",
            "insee_92b-ecarts-salaires": "none"
        }
    },
}

Processer(config).process()