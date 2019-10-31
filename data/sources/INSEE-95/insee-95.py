import os
import json
import pandas as pd
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
            "INSEE-95 - conseils municipaux.csv": "one_save",
            "INSEE-95 - temps partiel.csv": "one_save",
            "INSEE-95 - accès à l'emploi.csv": "one_save",
            "INSEE-95 - taux d'emploi.csv": "one_save",
            "INSEE-95 - taux de temps partiel.csv": "one_save",
            "INSEE-95 - part des cadres.csv": "one_save",
        },
    },
    "preprocesser": {
        'fns': {
            "INSEE-95 - conseils municipaux.csv": ["virg2point"],
            "INSEE-95 - temps partiel.csv": [],
            "INSEE-95 - accès à l'emploi.csv": ["virg2point"],
            "INSEE-95 - taux d'emploi.csv": ["virg2point"],
            "INSEE-95 - taux de temps partiel.csv": ["virg2point"],
            "INSEE-95 - part des cadres.csv": ["virg2point"],
        },
        'rename': {
            'country': 'pays',
            'year': 'annee',
            'indicator': 'nom',
            'value': 'valeur',
        },
    },
    "filter": {
        'filter_indicator_path': filter_indicator_path,
        'year': {
            "INSEE-95 - conseils municipaux.csv": 2010,
            "INSEE-95 - temps partiel.csv": 2010,
            "INSEE-95 - accès à l'emploi.csv": 2010,
            "INSEE-95 - taux d'emploi.csv": 2010,
            "INSEE-95 - taux de temps partiel.csv": 2010,
            "INSEE-95 - part des cadres.csv": 2010,
        }
    },
    "mapper": {
        'fns': {
            "INSEE-95 - conseils municipaux.csv": "proportion100",
            "INSEE-95 - temps partiel.csv": "diffFH_25",
            "INSEE-95 - accès à l'emploi.csv": "diffFH_20",
            "INSEE-95 - taux d'emploi.csv": "diffFH_10",
            "INSEE-95 - taux de temps partiel.csv": "diffFH_20",
            "INSEE-95 - part des cadres.csv": "diffFH_15",
        }
    },
    "translator": {
    },
    "postprocesser": {
        'fns': {
            "INSEE-95 - conseils municipaux.csv": "diff_perc",
            "INSEE-95 - temps partiel.csv": "diff_pp",
            "INSEE-95 - accès à l'emploi.csv": "diff_pp",
            "INSEE-95 - taux d'emploi.csv": "diff_pp",
            "INSEE-95 - taux de temps partiel.csv": "diff_pp",
            "INSEE-95 - part des cadres.csv": "diff_pp",
        }
    },
    "sorter": {
        'fns': {
            "INSEE-95 - conseils municipaux.csv": "none",
            "INSEE-95 - temps partiel.csv": "none",
            "INSEE-95 - accès à l'emploi.csv": "none",
            "INSEE-95 - taux d'emploi.csv": "none",
            "INSEE-95 - taux de temps partiel.csv": "none",
            "INSEE-95 - part des cadres.csv": "none",
        }
    },
}

Processer(config).process()
