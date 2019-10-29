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
            "Conditions de vie_Société.csv": "one_save",
            "Enseignement_Education.csv": "one_save",
            "Revenus_Salaires.csv": "one_save",
            "Travail_Emploi.csv": "one_save",
            "Conditions de vie_2015 - temps_sociaux.csv": "one_save",
            "marc-salair-net-mens-sexe-csp-2 - hor.csv": "one_save",
        },
    },
    "preprocesser": {
        'fns': {
            "Conditions de vie_Société.csv": ["virg2point"],
            "Enseignement_Education.csv": ["virg2point"],
            "Revenus_Salaires.csv": ["virg2point"],
            "Travail_Emploi.csv": ["virg2point"],
            "Conditions de vie_2015 - temps_sociaux.csv": [],
            "marc-salair-net-mens-sexe-csp-2 - hor.csv": ["virg2point", "remove_euro_and_perc", "percRel100"],
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
            "Conditions de vie_Société.csv": 2010,
            "Enseignement_Education.csv": 2010,
            "Revenus_Salaires.csv": 2010,
            "Travail_Emploi.csv": 2010,
            "Conditions de vie_2015 - temps_sociaux.csv": 1980,
            "marc-salair-net-mens-sexe-csp-2 - hor.csv": 1980,
        }
    },
    "mapper": {
        'fns': {
            "Conditions de vie_Société.csv": "diffFH_50",
            "Enseignement_Education.csv": "diffFH_20",
            "Revenus_Salaires.csv": "diffFH_20",
            "Travail_Emploi.csv": "diffFH_20",
            "Conditions de vie_2015 - temps_sociaux.csv": "diff_fm_minutes",
            "marc-salair-net-mens-sexe-csp-2 - hor.csv": "diffFH_20",
        }
    },
    "translator": {
    },
    "postprocesser": {
        'fns': {
            "Conditions de vie_Société.csv": "diff_pp",
            "Enseignement_Education.csv": "diff_pp",
            "Revenus_Salaires.csv": "diff_perc",
            "Travail_Emploi.csv": "diff_pp",
            "Conditions de vie_2015 - temps_sociaux.csv": "diff_minutes",
            "marc-salair-net-mens-sexe-csp-2 - hor.csv": "diff_perc_0v",
        }
    },
    "sorter": {
        'fns': {
            "Conditions de vie_Société.csv": "none",
            "Enseignement_Education.csv": "none",
            "Revenus_Salaires.csv": "none",
            "Travail_Emploi.csv": "none",
            "Conditions de vie_2015 - temps_sociaux.csv": "date_country",
            "marc-salair-net-mens-sexe-csp-2 - hor.csv": "date_country",
        }
    },
}

Processer(config).process()
