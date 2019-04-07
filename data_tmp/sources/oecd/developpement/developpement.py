import os
import json
import pandas as pd
from murs_invisibles import Processer


proc = Processer(
    read_path=os.path.dirname(os.path.realpath(__file__)),
    rename={
        'Pays': 'pays',
        'TIME': 'année',
        'VAR': 'formulation',
        'Value': 'value',
    },
    file_fn={
        # Titres fonciers détenus par les femmes
        'GIDDB2014_02042019001335690.csv': 'proportion1',
        # La représentation des femmes aux postes de direction
        'GIDDB2019_02042019002819783.csv': 'proportion1',
    },
    file_year={
        'GIDDB2014_02042019001335690.csv': 2010,
        'GIDDB2019_02042019002819783.csv': 2010,
    },
)


for name, fn in proc.file_fn.items():

    in_path = os.path.join(proc.read_path, name)

    # read data frame
    df = pd.read_csv(in_path, header=0, encoding='utf-8')

    # rename columns and drop rest
    df = df.rename(columns=proc.rename)[proc.rename.values()]

    # filter year
    df = df[df['année'] >= proc.file_year[name]]

    # create map value
    df['map_value'] = df.value.apply(fn)

    # filter pays
    df = df[df['pays'].apply(lambda x: x not in proc.filter_country)]

    # NO translate pays

    # encode pays
    df['pays'] = df['pays'].apply(lambda x: proc.encode(x))

    # translate formulation
    df['formulation'] = df['formulation'].apply(
        lambda x: proc.form_dict_en2fr[x])
    # encode formulation
    df['formulation'] = df['formulation'].apply(lambda x: proc.encode(x))

    # save
    proc.to_csv(df, in_path)
