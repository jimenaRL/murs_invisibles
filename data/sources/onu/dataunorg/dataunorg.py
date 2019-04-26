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
        'country': 'Unnamed: 1',
        'year': 'Year',
        'indicator': 'Series',
        'value': 'Value'
    },
    file_preprocess={
        'SYB61_T05_Seats held by Women in Parliament.csv': 'no_preprocess',
        # /!\ problem with ’ character /!\
        'SYB61_T06_Ratio of Girls to Boys in Education.csv': 'no_preprocess',
    },
    file_postprocess={
        'SYB61_T05_Seats held by Women in Parliament.csv': 'perc',
        'SYB61_T06_Ratio of Girls to Boys in Education.csv': 'ratio',
    },
    file_valuemap={
        'SYB61_T05_Seats held by Women in Parliament.csv': 'proportion100',
        'SYB61_T06_Ratio of Girls to Boys in Education.csv': 'women2men_ratio'
    },
    file_save={
        'SYB61_T05_Seats held by Women in Parliament.csv': 'one_save',
        'SYB61_T06_Ratio of Girls to Boys in Education.csv': 'one_save',
    },
    file_min_year={
        'SYB61_T05_Seats held by Women in Parliament.csv': 2010,
        'SYB61_T06_Ratio of Girls to Boys in Education.csv': 2010
    },
    country_filter_lang='en',
    country_lang='en2fr',
    indicator_lang='en2fr',
)

proc.process()
    