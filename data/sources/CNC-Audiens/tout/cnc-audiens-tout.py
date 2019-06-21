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
            "audiens_tout.csv": "one_save",
            "cnc_tout_doc_2_ecarts.csv": "one_save",
            "tout_docs_1_part_des_femmes.csv": "one_save",
        },
    },
    "preprocesser": {
        'fns': {
            "audiens_tout.csv": "no_process",
            "cnc_tout_doc_2_ecarts.csv": "no_process",
            "tout_docs_1_part_des_femmes.csv": "no_process",
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
            "audiens_tout.csv": "proportion100",
            "cnc_tout_doc_2_ecarts.csv": "ecart100",
            "tout_docs_1_part_des_femmes.csv": "proportion100",
        }
    },
    "filter": {
        'filter_indicator_path': None,
        'country_filter_lang': 'fr',
        'year': {
            "audiens_tout.csv": 2010,
            "cnc_tout_doc_2_ecarts.csv": 2010,
            "tout_docs_1_part_des_femmes.csv": 2010,
        }
    },
    "translator": {
        'country_lang': 'fr2fr',
        'indicator_lang': 'fr2fr',
    },
    "postprocesser": {
        'fns': {
            "audiens_tout.csv": "diff_perc",
            "cnc_tout_doc_2_ecarts.csv": "diff_perc",
            "tout_docs_1_part_des_femmes.csv": "perc",
        }
    },
}

Processer(config).process()
