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
        'country': 'Pays',
        'year': 'TIME',
        'indicator': 'Indicateur',
        'value': 'Value',
    },
    file_preprocess={
        'ENT4.csv': 'no_preprocess',
        'GENDER_ENT1_01042019230825609_remove_ENT4.csv': 'diff_wm',
    },
    file_postprocess={
        'ENT4.csv': 'perc',
        'GENDER_ENT1_01042019230825609_remove_ENT4.csv': 'diff_perc',

    },
    file_valuemap={
        'ENT4.csv': 'proportion1',
        'GENDER_ENT1_01042019230825609_remove_ENT4.csv': 'ecart100',  # or 'norm_wm',?
    },
    file_save={
        'ENT4.csv': 'one_save',
        'GENDER_ENT1_01042019230825609_remove_ENT4.csv': 'sep_save',
    },
    file_min_year={
        'ENT4.csv': 2010,
        'GENDER_ENT1_01042019230825609_remove_ENT4.csv': 2010,
    },
    country_filter_lang='fr',
    country_lang='fr2fr',
    indicator_lang='fr2fr',
)

proc.process()
