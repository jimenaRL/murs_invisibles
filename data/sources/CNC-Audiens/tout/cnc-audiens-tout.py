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
            #"cnc_tout_doc_2_ecarts.csv": "one_save",  # A VERIFIER SAISI !!!!!
            "tout_docs_1_part_des_femmes.csv": "one_save",
            "Audiens_études Stat Audiovisuel 2019-2016, Ecarts - Ecart culture mise à jour 2019.csv": "one_save",
            "Audiens_études Stat Audiovisuel 2019-2016, Part de femmes - Part de femmes Mise à jour 2017.csv": "one_save",
        },
    },
    "preprocesser": {
        'fns': {
            "audiens_tout.csv": ["no_process"],
            "cnc_tout_doc_2_ecarts.csv": ["no_process"],
            "tout_docs_1_part_des_femmes.csv": ["no_process"],
            "Audiens_études Stat Audiovisuel 2019-2016, Ecarts - Ecart culture mise à jour 2019.csv": ["remove_prop"],
            "Audiens_études Stat Audiovisuel 2019-2016, Part de femmes - Part de femmes Mise à jour 2017.csv": ["remove_prop"],
        },
        'rename': {
            'country': ['pays'],
            'year': ['annee'],
            'indicator': ['nom'],
            'value': ['valeur'],
        },
    },
    "mapper": {
        'fns': {
            "audiens_tout.csv": "proportion100",
            "cnc_tout_doc_2_ecarts.csv": "diffFH_50",
            "tout_docs_1_part_des_femmes.csv": "proportion100",
            "Audiens_études Stat Audiovisuel 2019-2016, Ecarts - Ecart culture mise à jour 2019.csv":  "diffFH_50",
            "Audiens_études Stat Audiovisuel 2019-2016, Part de femmes - Part de femmes Mise à jour 2017.csv": "proportion100",
       }
    },
    "filter": {
        'filter_indicator_path': None,
        'year': {
            "audiens_tout.csv": 2010,
            "cnc_tout_doc_2_ecarts.csv": 2010,
            "tout_docs_1_part_des_femmes.csv": 2010,
            "Audiens_études Stat Audiovisuel 2019-2016, Ecarts - Ecart culture mise à jour 2019.csv":  2010,
            "Audiens_études Stat Audiovisuel 2019-2016, Part de femmes - Part de femmes Mise à jour 2017.csv": 2010,
        }
    },
    "translator": {
    },
    "postprocesser": {
        'fns': {
            "audiens_tout.csv": "perc",
            "cnc_tout_doc_2_ecarts.csv": "perc_1v",
            "tout_docs_1_part_des_femmes.csv": "perc",
            "Audiens_études Stat Audiovisuel 2019-2016, Ecarts - Ecart culture mise à jour 2019.csv":  "diff_perc_0v",
            "Audiens_études Stat Audiovisuel 2019-2016, Part de femmes - Part de femmes Mise à jour 2017.csv": "perc",
        }
    },
    "sorter": {
        'fns': {
            "audiens_tout.csv": "none",
            "cnc_tout_doc_2_ecarts.csv": "none",
            "tout_docs_1_part_des_femmes.csv": "none",
            "Audiens_études Stat Audiovisuel 2019-2016, Ecarts - Ecart culture mise à jour 2019.csv":  "none",
            "Audiens_études Stat Audiovisuel 2019-2016, Part de femmes - Part de femmes Mise à jour 2017.csv": "none",
         }
    },
}

Processer(config).process()
