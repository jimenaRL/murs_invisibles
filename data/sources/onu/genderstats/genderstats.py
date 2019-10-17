import os
from murs_invisibles import Processer

config = {
    "base_path": os.path.dirname(os.path.realpath(__file__)),
    "origin_language": "en",
    "io": {
        "header": 1,
        "encoding": 'latin1',
        "fns": {
            '46 - Share of female police officers_data.csv': 'one_save',
        }
    },
    "preprocesser": {
        'fns': {
            '46 - Share of female police officers_data.csv': ['no_process'],
        },
        'rename': {
            'country': 'Country',
            'year': 'Year',
            'indicator': 'Indicator Name',
            'value': 'Value'
        },
    },
    "mapper": {
        'fns': {
            '46 - Share of female police officers_data.csv': 'proportion1',
        }
    },
    "filter": {
        'filter_indicator_path': None,
        'year': {
            '46 - Share of female police officers_data.csv': 2010,
        }
    },
    "translator": {
    },
    "postprocesser": {
        'fns': {
        '46 - Share of female police officers_data.csv': 'percX100',
        }
    },
    "sorter": {
        'fns': {
            '46 - Share of female police officers_data.csv': 'none',
        }
    },
}

Processer(config).process()
