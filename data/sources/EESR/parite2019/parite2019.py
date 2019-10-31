import os
import json
import pandas as pd
from murs_invisibles import Processer

filepath = os.path.dirname(os.path.realpath(__file__))


config = {
    "base_path": filepath,
    "origin_language": "fr",
    "io": {
        "header": 0,
        "encoding": "utf-8",
        "fns": {
            "parite2019_femmes-hommes.csv": "one_save",
        }
    },
    "preprocesser": {
        "fns": {
            "parite2019_femmes-hommes.csv": ["percRel100"],

        },
        "rename": {
            "country": "pays",
            "year": "annee",
            "indicator": "nom",
            "value": "part de femmes"
        }
    },
    "mapper": {
        "fns": {
            "parite2019_femmes-hommes.csv": "diffFH_20",
        }
    },
    "filter": {
        "filter_indicator_path": None,
        "year": {
            "parite2019_femmes-hommes.csv": 2010,
        }
    },
    "translator": {
    },
    "postprocesser": {
        "fns": {
            "parite2019_femmes-hommes.csv": "diff_perc",

        }
    },
    "sorter": {
        "fns": {
            "parite2019_femmes-hommes.csv": "none",
        }
    }
}


processer = Processer(config)

processer.process()
