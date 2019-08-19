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
            'GIDDB2014_02042019001335690.csv': 'one_save',
            'GIDDB2019_02042019002819783.csv': 'one_save',
        },
    },
    "preprocesser": {
        'fns': {
            'GIDDB2014_02042019001335690.csv': 'no_process',
            'GIDDB2019_02042019002819783.csv': 'no_process',
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
            'GIDDB2014_02042019001335690.csv': 'proportion1',
            # La représentation des femmes aux postes de direction
            'GIDDB2019_02042019002819783.csv': 'proportion1',
        }
    },
    "filter": {
        'filter_indicator_path': None,
        'country_filter_lang': 'fr',
        'year': {
            'GIDDB2014_02042019001335690.csv': 2010,
            'GIDDB2019_02042019002819783.csv': 2010,
        }
    },
    "translator": {
        'country_lang': 'fr2fr',
        'indicator_lang': 'fr2fr',
    },
    "postprocesser": {
        'fns': {
            'GIDDB2014_02042019001335690.csv': 'percX100',
            'GIDDB2019_02042019002819783.csv': 'percX100',
        }
    },
    "sorter": {
        'fns': {
            'GIDDB2014_02042019001335690.csv': 'none',
            'GIDDB2019_02042019002819783.csv': 'none',
        }
    },
}

Processer(config).process()
