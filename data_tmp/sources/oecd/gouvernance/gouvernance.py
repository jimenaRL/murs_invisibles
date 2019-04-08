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
        'country': 'Country',
        'year': 'Year',
        'indicator': 'Indicator',
        'value': 'Value',
    },
    file_preprocess={
        'GOV_2017_03042019165415175.csv': 'no_preprocess',
    },
    file_valuemap={
        'GOV_2017_03042019165415175.csv': 'proportion100',
    },
    file_min_year={
        'GOV_2017_03042019165415175.csv': 2010,
    },
    lang_in='en',
    lang_out='fr',
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

#     # translate pays
#     df['pays'] = df['pays'].apply(lambda x: proc.country_dict_en2fr[x])

#     # encode pays
#     df['pays'] = df['pays'].apply(lambda x: proc.encode(x))

#     # filter indicator
#     df = df[df['indicator'].apply(lambda x: x not in proc.filter_indicator)]

#     # translate indicator
#     df['indicator'] = df['indicator'].apply(
#         lambda x: proc.ind_en2fr[x])
#     # encode indicator
#     df['indicator'] = df['indicator'].apply(lambda x: proc.encode(x))

#     # save
#     proc.to_csv(df, in_path)
