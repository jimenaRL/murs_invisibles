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
        'SYB61_T06_Ratio of Girls to Boys in Education.csv': 'no_preprocess',
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
    lang_in='en',
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
#     df = df[df['année'] >= proc.file_min_year[name]]

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
