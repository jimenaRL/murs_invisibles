import os
import json
import pandas as pd
from murs_invisibles import Processer


file_dir = os.path.dirname(os.path.realpath(__file__))
filter_indicator_path = os.path.join(file_dir, 'indicator_filter.txt')

proc = Processer(
    read_path=file_dir,
    filter_indicator_path=filter_indicator_path,
    header=0,
    encoding='utf-8',
    rename={
        'country': 'Country',
        'year': 'Year',
        'indicator': 'Indicator',
        'value': 'Value',
    },
    file_preprocess={
        'GOV_2017_03042019165415175.csv': 'no_preprocess',
    },
    file_postprocess={
        'GOV_2017_03042019165415175.csv': 'perc',
    },
    file_valuemap={
        'GOV_2017_03042019165415175.csv': 'proportion100',
    },
    file_save={
        'GOV_2017_03042019165415175.csv': 'sep_save',
    },
    file_min_year={
        'GOV_2017_03042019165415175.csv': 2010,
    },
    country_filter_lang='en',
    country_lang='en2fr',
    indicator_lang='en2fr',
)

proc.process()
