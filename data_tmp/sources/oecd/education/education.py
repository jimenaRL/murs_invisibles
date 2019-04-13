import os
import json
import pandas as pd
from murs_invisibles import Processer


file_dir = os.path.dirname(os.path.realpath(__file__))

proc = Processer(
    read_path=file_dir,
    filter_indicator_path=None,
    header=0,
    encoding='utf-8',
    rename={
        'country': 'Pays',
        'year': 'TIME',
        'indicator': 'Indicateur',
    },
    file_preprocess={
        # All emploi
        'GENDER_EDU_29102017131322363.csv': 'womenANDmen',
    },
    file_valuemap={
        # All emploi
        'GENDER_EDU_29102017131322363.csv': 'proportion100',
    },
    file_save={
        'GENDER_EDU_29102017131322363.csv': 'sep_save',
    },
    file_min_year={
        'GENDER_EDU_29102017131322363.csv': 2010,
    },
    country_filter_lang='fr',
    country_lang='fr2fr',
    indicator_lang='en2fr',
)

proc.process()
