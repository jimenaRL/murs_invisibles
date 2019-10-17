import os
import json
import pandas as pd
from murs_invisibles import Processer


config = {
    "base_path": os.path.dirname(os.path.realpath(__file__)),
    "origin_language": "fr",
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
            "audiens_tout.csv": ["no_process"],
            "cnc_tout_doc_2_ecarts.csv": ["no_process"],
            "tout_docs_1_part_des_femmes.csv": ["no_process"],
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
            "cnc_tout_doc_2_ecarts.csv": "diffFH_50",
            "tout_docs_1_part_des_femmes.csv": "proportion100",
        }
    },
    "filter": {
        'filter_indicator_path': None,
        'year': {
            "audiens_tout.csv": 2010,
            "cnc_tout_doc_2_ecarts.csv": 2010,
            "tout_docs_1_part_des_femmes.csv": 2010,
        }
    },
    "translator": {
    },
    "postprocesser": {
        'fns': {
            "audiens_tout.csv": "perc",
            "cnc_tout_doc_2_ecarts.csv": "diff_pp",
            "tout_docs_1_part_des_femmes.csv": "perc",
        }
    },
    "sorter": {
        'fns': {
            "audiens_tout.csv": "none",
            "cnc_tout_doc_2_ecarts.csv": "none",
            "tout_docs_1_part_des_femmes.csv": "none",
        }
    },
}

Processer(config).process()
