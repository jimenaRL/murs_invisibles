import os
from murs_invisibles import Processer


file_dir = os.path.dirname(os.path.realpath(__file__))
filter_indicator_path = os.path.join(file_dir, 'indicator_filter.txt')

config = {
    "base_path": os.path.dirname(os.path.realpath(__file__)),
    "origin_language": "en",
    "io": {
        "header": 0,
        "encoding": 'utf-8',
        "fns": {
            'GOV_2017_03042019165415175.csv': 'sep_save',
            'DP_LIVE_27092021102520552-Women-ministers-Percentage-2005-2019.csv': 'one_save',
            'DP_LIVE_27092021102630661-Women-parliamentarians-Percentage-2002-2019.csv': 'one_save',
        },
    },
    "preprocesser": {
        'fns': {
            'GOV_2017_03042019165415175.csv': ['no_process'],
            'DP_LIVE_27092021102520552-Women-ministers-Percentage-2005-2019.csv': ['no_process'],
            'DP_LIVE_27092021102630661-Women-parliamentarians-Percentage-2002-2019.csv': ['no_process'],
        },
        'rename': {
            'country': ['Country', 'LOCATION'],
            'year': ['Year', 'TIME'],
            'indicator': ['Indicator', 'SUBJECT'],
            'value': ['Value'],
        },
    },
    "mapper": {
        'fns': {
            'GOV_2017_03042019165415175.csv': 'proportion100',
            'DP_LIVE_27092021102520552-Women-ministers-Percentage-2005-2019.csv': 'proportion100',
            'DP_LIVE_27092021102630661-Women-parliamentarians-Percentage-2002-2019.csv': 'proportion100',
        }
    },
    "filter": {
        'filter_indicator_path': filter_indicator_path,
        'year': {
            'GOV_2017_03042019165415175.csv': 2015,
            'DP_LIVE_27092021102520552-Women-ministers-Percentage-2005-2019.csv': 2015,
            'DP_LIVE_27092021102630661-Women-parliamentarians-Percentage-2002-2019.csv': 2016,
        }
    },
    "translator": {
    },
    "postprocesser": {
        'fns': {
            'GOV_2017_03042019165415175.csv': 'perc',
            'DP_LIVE_27092021102520552-Women-ministers-Percentage-2005-2019.csv': 'perc',
            'DP_LIVE_27092021102630661-Women-parliamentarians-Percentage-2002-2019.csv': 'perc',
        }
    },
    "sorter": {
        'fns': {
            'GOV_2017_03042019165415175.csv': 'date_country',
            'DP_LIVE_27092021102520552-Women-ministers-Percentage-2005-2019.csv': 'date_country',
            'DP_LIVE_27092021102630661-Women-parliamentarians-Percentage-2002-2019.csv': 'date_country',
        }
    },
}

Processer(config).process()
