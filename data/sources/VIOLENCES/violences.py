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
            # "stop-violences - Violences au sein du couple et violences sexuelles 2018.csv": "one_save",
            "Etude nationale sur les morts violentes au sein du couple - 2014-2018.csv": "one_save",
            # "INED - T3 Victimes estimés de violences sexuelles dans les 12 derniers mois.csv": "one_save",
            # "INED - T4 Victimes violences sexuelles dans l'année.csv": "one_save",
            # "INED - T5 violences sexuelles  par catégorie juridique et espace de vie etdans les 12 derniers mois .csv": "one_save",
            # "INED - T6 Victimes violences sexuelles au cours de la vie.csv": "one_save",
            # "INED - T8 Victimes d'agressions sexuelles dans les 12 derniers mois, par age.csv": "one_save",

        },
    },
    "preprocesser": {
        'fns': {
            "stop-violences - Violences au sein du couple et violences sexuelles 2018.csv": ["remove_prop"],
            "Etude nationale sur les morts violentes au sein du couple - 2014-2018.csv": ["remove_prop"],
            "INED - T3 Victimes estimés de violences sexuelles dans les 12 derniers mois.csv": [],
            "INED - T4 Victimes violences sexuelles dans l'année.csv": [],
            "INED - T5 violences sexuelles  par catégorie juridique et espace de vie etdans les 12 derniers mois .csv": ["remove_google_sheet_nan"],
            "INED - T6 Victimes violences sexuelles au cours de la vie.csv": ["remove_google_sheet_nan"],
            "INED - T8 Victimes d'agressions sexuelles dans les 12 derniers mois, par age.csv": ["remove_google_sheet_nan"],
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
            "stop-violences - Violences au sein du couple et violences sexuelles 2018.csv": 2010,
            "Etude nationale sur les morts violentes au sein du couple - 2014-2018.csv": 2010,
            "INED - T3 Victimes estimés de violences sexuelles dans les 12 derniers mois.csv": 2010,
            "INED - T4 Victimes violences sexuelles dans l'année.csv": 2010,
            "INED - T5 violences sexuelles  par catégorie juridique et espace de vie etdans les 12 derniers mois .csv": 2010,
            "INED - T6 Victimes violences sexuelles au cours de la vie.csv": 2010,
            "INED - T8 Victimes d'agressions sexuelles dans les 12 derniers mois, par age.csv": 2010,
        }
    },
    "mapper": {
        'fns': {
            "stop-violences - Violences au sein du couple et violences sexuelles 2018.csv": "proportion100",
            "Etude nationale sur les morts violentes au sein du couple - 2014-2018.csv": "proportion100",
            "INED - T3 Victimes estimés de violences sexuelles dans les 12 derniers mois.csv":  "proportion100",
            "INED - T4 Victimes violences sexuelles dans l'année.csv":  "proportion100",
            "INED - T5 violences sexuelles  par catégorie juridique et espace de vie etdans les 12 derniers mois .csv":  "proportion100",
            "INED - T6 Victimes violences sexuelles au cours de la vie.csv":  "proportion100",
            "INED - T8 Victimes d'agressions sexuelles dans les 12 derniers mois, par age.csv":  "proportion100",
        }
    },
    "translator": {
    },
    "postprocesser": {
        'fns': {
            "stop-violences - Violences au sein du couple et violences sexuelles 2018.csv": "perc",
            "Etude nationale sur les morts violentes au sein du couple - 2014-2018.csv": "perc",
            "INED - T3 Victimes estimés de violences sexuelles dans les 12 derniers mois.csv":  "perc",
            "INED - T4 Victimes violences sexuelles dans l'année.csv":  "perc",
            "INED - T5 violences sexuelles  par catégorie juridique et espace de vie etdans les 12 derniers mois .csv":  "perc",
            "INED - T6 Victimes violences sexuelles au cours de la vie.csv":  "perc",
            "INED - T8 Victimes d'agressions sexuelles dans les 12 derniers mois, par age.csv":  "perc",
        }
    },
    "sorter": {
        'fns': {
            "stop-violences - Violences au sein du couple et violences sexuelles 2018.csv": "none",
            "Etude nationale sur les morts violentes au sein du couple - 2014-2018.csv": "none",
            "INED - T3 Victimes estimés de violences sexuelles dans les 12 derniers mois.csv":  "none",
            "INED - T4 Victimes violences sexuelles dans l'année.csv":  "none",
            "INED - T5 violences sexuelles  par catégorie juridique et espace de vie etdans les 12 derniers mois .csv":  "none",
            "INED - T6 Victimes violences sexuelles au cours de la vie.csv":  "none",
            "INED - T8 Victimes d'agressions sexuelles dans les 12 derniers mois, par age.csv":  "none",
        }
    },
}

Processer(config).process()
