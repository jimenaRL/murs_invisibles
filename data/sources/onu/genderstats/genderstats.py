import os
import json
import pandas as pd
from murs_invisibles import Processer


proc = Processer(
    read_path=os.path.dirname(os.path.realpath(__file__)),
    filter_indicator_path=None,
    header=1,
    encoding='latin1',
    rename={
        'country': 'Country',
        'year': 'Year',
        'indicator': 'Indicator Name',
        'value': 'Value'
    },
    file_preprocess={
        '46 - Share of female police officers_data.csv': 'no_preprocess',
    },
    file_postprocess={
        '46 - Share of female police officers_data.csv': 'perc',
    },
    file_valuemap={
        '46 - Share of female police officers_data.csv': 'proportion1',
    },
    file_save={
        '46 - Share of female police officers_data.csv': 'one_save',
    },
    file_min_year={
        '46 - Share of female police officers_data.csv': 2010,
    },
    country_filter_lang='en',
    country_lang='en2fr',
    indicator_lang='en2fr',
)

proc.process()
