import os
import json
import pandas as pd
from murs_invisibles import Processer


config = {
    "data_path": os.path.dirname(os.path.realpath(__file__)),
    "io": {
        "header": 0,
        "encoding": 'utf-8',
        "fns": {
            "18_indicateurs_REG.csv": "one_save",
            "conditions_de_vie.csv": "one_save",
            # "ecarts_salaires_horaires.csv": "one_save",
            "retraite_et_revenus.csv": "one_save",
        },
    },
    "preprocesser": {
        'fns': {
            "18_indicateurs_REG.csv": "no_process",
            "conditions_de_vie.csv": "no_process",
            # "ecarts_salaires_horaires.csv": "",
            "retraite_et_revenus.csv": "no_process",
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
            "18_indicateurs_REG.csv": "ecart100",
            "conditions_de_vie.csv": "conditions_de_vie",
            # "ecarts_salaires_horaires.csv": "",
            "retraite_et_revenus.csv": "ecart100",
        }
    },
    "filter": {
        'filter_indicator_path': None,
        'country_filter_lang': 'fr',
        'year': {
            "18_indicateurs_REG.csv": 2010,
            "conditions_de_vie.csv": 2010,
            # "ecarts_salaires_horaires.csv": 2010,
            "retraite_et_revenus.csv": 2010,
        }
    },
    "translator": {
        'country_lang': 'fr2fr',
        'indicator_lang': 'fr2fr',
    },
    "postprocesser": {
        'fns': {
            "18_indicateurs_REG.csv": "no_process",
            "conditions_de_vie.csv": "conditions_de_vie",
            # "ecarts_salaires_horaires.csv": "",
            "retraite_et_revenus.csv": "diff_perc",
        }
    },
}

Processer(config).process()