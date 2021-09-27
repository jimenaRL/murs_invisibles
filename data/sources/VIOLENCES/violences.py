import os
import json
import pandas as pd
from murs_invisibles import Processer

file_dir = os.path.dirname(os.path.realpath(__file__))
filter_indicator_path = os.path.join(file_dir, 'indicator_filter.txt')

config = {
    "base_path": os.path.dirname(os.path.realpath(__file__)),
    "origin_language": "fr",
    "merge": {},
    "io": {
        "header": 0,
        "encoding": 'utf-8',
        'fns': {
            "stop-violences - Autrices Violences au sein du couple 2018.csv": "one_save",
            "stop-violences - STOP VIOLENCE 2018 Victimes + INED T8.csv": "one_save",
            "Etude nationale sur les morts violentes au sein du couple+ INED Virage T6 - Et NAT violence + INED T6.csv": "one_save",
            "INED - T5 + T3 violences sexuelles par cat juridique dans les 12 derniers mois.csv": "one_save",
            "INED - INED T4 Viol sex + Etude Nat Viol sex 2018 2020.csv": "one_save",
        }, 
    },
    "preprocesser": {
        'fns': {
            "stop-violences - Autrices Violences au sein du couple 2018.csv": ["remove_prop"],
            "stop-violences - STOP VIOLENCE 2018 Victimes + INED T8.csv": ["remove_prop"],
            "Etude nationale sur les morts violentes au sein du couple+ INED Virage T6 - Et NAT violence + INED T6.csv": ["remove_prop"],
            "INED - T5 + T3 violences sexuelles par cat juridique dans les 12 derniers mois.csv": [],
            "INED - INED T4 Viol sex + Etude Nat Viol sex 2018 2020.csv": [],
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
            "stop-violences - Autrices Violences au sein du couple 2018.csv": 2010,
            "stop-violences - STOP VIOLENCE 2018 Victimes + INED T8.csv": 2010,
            "Etude nationale sur les morts violentes au sein du couple+ INED Virage T6 - Et NAT violence + INED T6.csv": 2010,
            "INED - T5 + T3 violences sexuelles par cat juridique dans les 12 derniers mois.csv": 2010,
            "INED - INED T4 Viol sex + Etude Nat Viol sex 2018 2020.csv": 2010,
        }
    },
    "mapper": {
        'fns': {
            "stop-violences - Autrices Violences au sein du couple 2018.csv": "proportion100",
            "stop-violences - STOP VIOLENCE 2018 Victimes + INED T8.csv": "proportion100",
            "Etude nationale sur les morts violentes au sein du couple+ INED Virage T6 - Et NAT violence + INED T6.csv": "proportion100",
            "INED - T5 + T3 violences sexuelles par cat juridique dans les 12 derniers mois.csv":  "proportion100",
            "INED - INED T4 Viol sex + Etude Nat Viol sex 2018 2020.csv":  "proportion100",
        }
    },
    "translator": {
    },
    "postprocesser": {
        'fns': {
            "stop-violences - Autrices Violences au sein du couple 2018.csv": "perc",
            "stop-violences - STOP VIOLENCE 2018 Victimes + INED T8.csv": "perc",
            "Etude nationale sur les morts violentes au sein du couple+ INED Virage T6 - Et NAT violence + INED T6.csv": "perc",
            "INED - T5 + T3 violences sexuelles par cat juridique dans les 12 derniers mois.csv":  "perc",
            "INED - INED T4 Viol sex + Etude Nat Viol sex 2018 2020.csv":  "perc",
            "INED - T5 violences sexuelles  par catégorie juridique et espace de vie etdans les 12 derniers mois .csv":  "perc",
            "INED - T6 Victimes violences sexuelles au cours de la vie.csv":  "perc",
            "INED - T8 Victimes d'agressions sexuelles dans les 12 derniers mois, par age.csv":  "perc",
        }
    },
    "sorter": {
        'fns': {
            "stop-violences - Autrices Violences au sein du couple 2018.csv": "none",
            "stop-violences - STOP VIOLENCE 2018 Victimes + INED T8.csv": "none",
            "Etude nationale sur les morts violentes au sein du couple+ INED Virage T6 - Et NAT violence + INED T6.csv": "none",
            "INED - T5 + T3 violences sexuelles par cat juridique dans les 12 derniers mois.csv":  "none",
            "INED - INED T4 Viol sex + Etude Nat Viol sex 2018 2020.csv":  "none",
        }
    },
}

Processer(config).process()
