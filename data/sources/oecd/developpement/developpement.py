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
        'country': 'Pays',
        'year': 'TIME',
        'indicator': 'VAR',
        'value': 'Value',
    },
    file_preprocess={
        'GIDDB2014_02042019001335690.csv': 'no_preprocess',
        'GIDDB2019_02042019002819783.csv': 'no_preprocess',
    },
    file_postprocess={
        'GIDDB2014_02042019001335690.csv': 'percX100',
        'GIDDB2019_02042019002819783.csv': 'percX100',
    },
    file_valuemap={
        # Titres fonciers détenus par les femmes
        'GIDDB2014_02042019001335690.csv': 'proportion1',
        # La représentation des femmes aux postes de direction
        'GIDDB2019_02042019002819783.csv': 'proportion1',
    },
    file_save={
        'GIDDB2014_02042019001335690.csv': 'one_save',
        'GIDDB2019_02042019002819783.csv': 'one_save',
    },
    file_min_year={
        'GIDDB2014_02042019001335690.csv': 2010,
        'GIDDB2019_02042019002819783.csv': 2010,
    },
    country_filter_lang='fr',
    country_lang='fr2fr',
    indicator_lang='fr2fr',
)

proc.process()
