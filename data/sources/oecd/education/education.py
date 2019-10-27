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
            "GENDER_EDU_29102017131322363.csv": "sep_save"
        }
    },
    "preprocesser": {
        "fns": {
            "GENDER_EDU_29102017131322363.csv": ["get_wm", "diffFH"]
        },
        "rename": {
            "country": "Pays",
            "year": "TIME",
            "indicator": "Indicateur",
            "value": "Value"
        }
    },
    "mapper": {
        "fns": {
            "GENDER_EDU_29102017131322363.csv": "diffFH_20"
        }
    },
    "filter": {
        "origin_language": "fr",
        "filter_indicator_path": None,
        "year": {
            "GENDER_EDU_29102017131322363.csv": 2010
        }
    },
    "translator": {
        "indicator_origin_language": "en",
        "country_origin_language": "fr"
    },
    "postprocesser": {
        "fns": {
            "GENDER_EDU_29102017131322363.csv": "diff_pp"
        }
    },
    "sorter": {
        "fns": {
            "GENDER_EDU_29102017131322363.csv": "date_country"
        }
    }
}



processer = Processer(config)

processer.process()
