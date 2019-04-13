import os
import json
import pandas as pd
from murs_invisibles import Processer


proc = Processer(
    read_path=os.path.dirname(os.path.realpath(__file__)),
    filter_indicator_path=None,
    header=0,
    encoding='utf-8',
    rename={
        'country': 'pays',
        'year': 'annee',
        'indicator': 'formulation',
        'value': 'value'
    },
    file_preprocess={
        'minist_dossier.csv': 'remove_prop',
    },
    file_valuemap={
        'minist_dossier.csv': 'proportion100',
    },
    file_save={
        'minist_dossier.csv': 'one_save',
    },
    file_min_year={
        'minist_dossier.csv': 2010,
    },
    country_filter_lang='fr',
    country_lang='fr2fr',
    indicator_lang='fr2fr',
)

proc.process()
