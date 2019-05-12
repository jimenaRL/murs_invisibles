import os
from murs_invisibles import Processer

config = {
    "data_path": os.path.dirname(os.path.realpath(__file__)),
    "io": {
        "header": 1,
        "encoding": 'latin1',
        "fns": {
            '46 - Share of female police officers_data.csv': 'one_save',
        }
    },
    "preprocesser": {
        'fns': {
            '46 - Share of female police officers_data.csv': 'no_process',
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
        'country_filter_lang': 'en',
        'year': {
            '46 - Share of female police officers_data.csv': 2010,
        }
    },
    "translator": {
        'country_lang': 'en2fr',
        'indicator_lang': 'en2fr',
    },
    "postprocesser": {
        'fns': {
        '46 - Share of female police officers_data.csv': 'perc',
        }
    },
}

Processer(config).process()
