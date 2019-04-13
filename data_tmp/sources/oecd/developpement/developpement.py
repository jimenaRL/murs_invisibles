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

# for name, fn in proc.file_valuemap.items():

#     in_path = os.path.join(proc.read_path, name)

#     # read data frame
#     df = pd.read_csv(in_path, header=0, encoding='utf-8')

#     # rename columns and drop rest
#     df = df.rename(columns=proc.rename)[proc.rename.values()]

#     # filter year
#     df = df[df['année'] >= proc.file_year[name]]

#     # create map value
#     df['map_value'] = df.value.apply(fn)

#     # filter pays
#     df = df[df['pays'].apply(lambda x: x not in proc.filter_country)]

#     # NO translate pays

#     # encode pays
#     df['pays'] = df['pays'].apply(lambda x: proc.encode(x))

#     # translate formulation
#     df['formulation'] = df['formulation'].apply(
#         lambda x: proc.ind_en2fr[x])
#     # encode formulation
#     df['formulation'] = df['formulation'].apply(lambda x: proc.encode(x))

#     # save
#     proc.to_csv(df, in_path)
