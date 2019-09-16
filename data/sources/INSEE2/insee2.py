import os
import json
import pandas as pd
from murs_invisibles import Processer


config = {
    "base_path": os.path.dirname(os.path.realpath(__file__)),
    "origin_language": "fr",
    "target_language": "es",
    "io": {
        "header": 0,
        "encoding": 'utf-8',
        'fns': {
            "Conditions de vie_Société.csv": "one_save",
            "Enseignement_Education.csv": "one_save",
            "Revenus_Salaires.csv": "one_save",
            "Travail_Emploi.csv": "one_save",
        },
    },
    "preprocesser": {
        'fns': {
            "Conditions de vie_Société.csv": "virg2point",
            "Enseignement_Education.csv": "virg2point",
            "Revenus_Salaires.csv": "virg2point",
            "Travail_Emploi.csv": "virg2point",
        },
        'rename': {
            'country': 'pays',
            'year': 'annee',
            'indicator': 'nom',
            'value': 'valeur',
        },
    },
    "mapper": {
        'fns': {
            "Conditions de vie_Société.csv": "diffFH_100",
            "Enseignement_Education.csv": "diffFH_10",
            "Revenus_Salaires.csv": "diffFH_100",
            "Travail_Emploi.csv": "diffFH_20",
        }
    },
    "filter": {
        'filter_indicator_path': None,
        'year': {
            "Conditions de vie_Société.csv": 2010,
            "Enseignement_Education.csv": 2010,
            "Revenus_Salaires.csv": 2010,
            "Travail_Emploi.csv": 2010,

        }
    },
    "translator": {
    },
    "postprocesser": {
        'fns': {
            "Conditions de vie_Société.csv": "diff_pp",
            "Enseignement_Education.csv": "diff_pp",
            "Revenus_Salaires.csv": "diff_pp",
            "Travail_Emploi.csv": "diff_pp",
        }
    },
    "sorter": {
        'fns': {
            "Conditions de vie_Société.csv": "none",
            "Enseignement_Education.csv": "none",
            "Revenus_Salaires.csv": "none",
            "Travail_Emploi.csv": "none",
        }
    },
}

Processer(config).process()
