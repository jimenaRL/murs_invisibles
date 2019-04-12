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
    lang_in='fr',
    lang_out='fr',
)



proc.process()

# for name, fn in proc.file_valuemap.items():

#     in_path = os.path.join(proc.read_path, name)

#     # read data frame
#     df = pd.read_csv(in_path, header=1, encoding='latin1')

#     # rename columns and drop rest
#     df = df.rename(columns=proc.rename)[proc.rename.values()]

#     # filter year
#     df = df[df['année'] >= proc.file_year[name]]

#     # create map value
#     df['map_value'] = df.value.apply(fn)

#     # filter pays
#     df = df[df['pays'].apply(lambda x: x not in proc.filter_country)]
#     # translate pays
#     df['pays'] = df['pays'].apply(lambda x: proc.country_dict_en2fr[x])
#     # encode pays
#     df['pays'] = df['pays'].apply(lambda x: proc.encode(x))

#     # translate indicator
#     df['indicator'] = df['indicator'].apply(
#         lambda x: proc.ind_en2fr[x])
#     # encode indicator
#     df['indicator'] = df['indicator'].apply(lambda x: proc.encode(x))

#     # save
#     proc.to_csv(df, in_path)
