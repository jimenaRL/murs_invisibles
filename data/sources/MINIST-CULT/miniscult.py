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
            "OBS_GROUP3_arts.csv": "one_save",
            "OBS_GROUP4_TV.csv": "one_save",
            "Observatoire_GROUP1_part.csv": "one_save",
            "Observatoire_GROUP1_ecarts.csv": "one_save",
            "Observatoire_group2_TH_.csv": "one_save",
        },
    },
    "preprocesser": {
        'fns': {
            "OBS_GROUP3_arts.csv": "remove_prop",
            "OBS_GROUP4_TV.csv": "remove_prop",
            "Observatoire_GROUP1_part.csv": "remove_prop",
            "Observatoire_GROUP1_ecarts.csv": "remove_prop",
            "Observatoire_group2_TH_.csv": "remove_prop",
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
            "OBS_GROUP3_arts.csv": "proportion100",
            "OBS_GROUP4_TV.csv": "proportion100",
            "Observatoire_GROUP1_part.csv": "proportion100",
            "Observatoire_GROUP1_ecarts.csv": "proportion100",
            "Observatoire_group2_TH_.csv": "proportion100",
        }
    },
    "filter": {
        'filter_indicator_path': None,
        'country_filter_lang': 'fr',
        'year': {
            "OBS_GROUP3_arts.csv": 2010,
            "OBS_GROUP4_TV.csv": 2010,
            "Observatoire_GROUP1_part.csv": 2010,
            "Observatoire_GROUP1_ecarts.csv": 2010,
            "Observatoire_group2_TH_.csv": 2010
        }
    },
    "translator": {
        'country_lang': 'fr2fr',
        'indicator_lang': 'fr2fr',
    },
    "postprocesser": {
        'fns': {
            "OBS_GROUP3_arts.csv": "perc",
            "OBS_GROUP4_TV.csv": "perc",
            "Observatoire_GROUP1_part.csv": "perc",
            "Observatoire_GROUP1_ecarts.csv": "diff_perc",
            "Observatoire_group2_TH_.csv": "perc",
        }
    },
    "sorter": {
        'fns': {
            "OBS_GROUP3_arts.csv": "none",
            "OBS_GROUP4_TV.csv": "none",
            "Observatoire_GROUP1_part.csv": "none",
            "Observatoire_GROUP1_ecarts.csv": "none",
            "Observatoire_group2_TH_.csv": "none",
        }
    },
}

Processer(config).process()
