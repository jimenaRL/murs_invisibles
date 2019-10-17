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
            'GIDDB2014_titres_fonciers.csv': 'one_save',
            'GIDDB2019_poste_de_direction.csv': 'one_save',
        },
    },
    "preprocesser": {
        'fns': {
            'GIDDB2014_titres_fonciers.csv': 'no_process',
            'GIDDB2019_poste_de_direction.csv': 'no_process',
        },
        'rename': {
            'country': 'Pays',
            'year': 'TIME',
            'indicator': 'VAR',
            'value': 'Value',
        },
    },
    "mapper": {
        'fns': {
            # Titres fonciers détenus par les femmes
            'GIDDB2014_titres_fonciers.csv': 'proportion1',
            # La représentation des femmes aux postes de direction
            'GIDDB2019_poste_de_direction.csv': 'proportion1',
        }
    },
    "filter": {
        'filter_indicator_path': None,
        'year': {
            'GIDDB2014_titres_fonciers.csv': 2010,
            'GIDDB2019_poste_de_direction.csv': 2010,
        }
    },
    "translator": {
    },
    "postprocesser": {
        'fns': {
            'GIDDB2014_titres_fonciers.csv': 'percX100',
            'GIDDB2019_poste_de_direction.csv': 'percX100',
        }
    },
    "sorter": {
        'fns': {
            'GIDDB2014_titres_fonciers.csv': 'none',
            'GIDDB2019_poste_de_direction.csv': 'none',
        }
    },
}

Processer(config).process()
