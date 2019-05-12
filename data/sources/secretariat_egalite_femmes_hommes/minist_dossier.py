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
        'country': 'pays',
        'year': 'annee',
        'indicator': 'formulation',
        'value': 'value'
    },
    file_preprocess={
        'minist_dossier.csv': 'remove_prop',
    },
    file_postprocess={
        'minist_dossier.csv': 'perc',
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