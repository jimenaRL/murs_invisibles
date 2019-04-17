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
    sep='\t',
    rename={
        'country': 'country',
        'year': 'year',
        'indicator': 'indicator',
        'value': 'value'
    },
    file_preprocess={
        'insee_educ/cond-educ-dip-eleve-age-sexe-2.tsv': 'remove_prop',
    },
    file_postprocess={
        'insee_educ/cond-educ-dip-eleve-age-sexe-2.tsv': 'perc',
    },
    file_valuemap={
        'insee_educ/cond-educ-dip-eleve-age-sexe-2.tsv': 'proportion100',
    },
    file_save={
        'insee_educ/cond-educ-dip-eleve-age-sexe-2.tsv': 'one_save',
    },
    file_min_year={
        'insee_educ/cond-educ-dip-eleve-age-sexe-2.tsv': 2014,
    },
    country_filter_lang='fr',
    country_lang='fr2fr',
    indicator_lang='fr2fr',
)

proc.process()
