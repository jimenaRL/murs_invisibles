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
            "Observatoire - OBS_GROUP3_arts.csv": "one_save",
            "Observatoire - OBS_GROUP4_TV.csv": "one_save",
            "Observatoire - Observatoire_GROUP1_part.csv": "one_save",
            "Observatoire - Observatoire_GROUP1_ecarts.csv": "one_save",
            "Observatoire - Observatoire_group2_TH_.csv": "one_save",
            "Observatoire - OBS_GROUP5_arts culture.csv": "one_save",
        },
    },
    "preprocesser": {
        'fns': {
            "Observatoire - OBS_GROUP3_arts.csv": ["remove_prop"],
            "Observatoire - OBS_GROUP4_TV.csv": ["remove_prop"],
            "Observatoire - Observatoire_GROUP1_part.csv": ["remove_prop"],
            "Observatoire - Observatoire_GROUP1_ecarts.csv": ["remove_prop"],
            "Observatoire - Observatoire_group2_TH_.csv": ["remove_prop"],
            "Observatoire - OBS_GROUP5_arts culture.csv": ["remove_prop"]
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
            "Observatoire - OBS_GROUP3_arts.csv": "proportion100",
            "Observatoire - OBS_GROUP4_TV.csv": "proportion100",
            "Observatoire - Observatoire_GROUP1_part.csv": "proportion100",
            "Observatoire - Observatoire_GROUP1_ecarts.csv": "proportion100",
            "Observatoire - Observatoire_group2_TH_.csv": "proportion100",
            "Observatoire - OBS_GROUP5_arts culture.csv": "proportion100"
        }
    },
    "filter": {
        'filter_indicator_path': None,
        'year': {
            "Observatoire - OBS_GROUP3_arts.csv": 2010,
            "Observatoire - OBS_GROUP4_TV.csv": 2010,
            "Observatoire - Observatoire_GROUP1_part.csv": 2010,
            "Observatoire - Observatoire_GROUP1_ecarts.csv": 2010,
            "Observatoire - Observatoire_group2_TH_.csv": 2010,
            "Observatoire - OBS_GROUP5_arts culture.csv": 2010
        }
    },
    "translator": {
    },
    "postprocesser": {
        'fns': {
            "Observatoire - OBS_GROUP3_arts.csv": "perc",
            "Observatoire - OBS_GROUP4_TV.csv": "perc",
            "Observatoire - Observatoire_GROUP1_part.csv": "perc",
            "Observatoire - Observatoire_GROUP1_ecarts.csv": "diff_perc",
            "Observatoire - Observatoire_group2_TH_.csv": "perc",
            "Observatoire - OBS_GROUP5_arts culture.csv": "perc"
        }
    },
    "sorter": {
        'fns': {
            "Observatoire - OBS_GROUP3_arts.csv": "none",
            "Observatoire - OBS_GROUP4_TV.csv": "none",
            "Observatoire - Observatoire_GROUP1_part.csv": "none",
            "Observatoire - Observatoire_GROUP1_ecarts.csv": "none",
            "Observatoire - Observatoire_group2_TH_.csv": "none",
            "Observatoire - OBS_GROUP5_arts culture.csv": "none"
        }
    },
}

Processer(config).process()
