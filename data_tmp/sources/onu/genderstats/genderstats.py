import os
import json
import pandas as pd
from murs_invisibles import Processer


proc = Processer()
proc.read_path = os.path.dirname(os.path.realpath(__file__))
proc.rename = {
    'Country': 'pays',
    'Year': 'année',
    'Indicator Name': 'formulation',
    'Value': 'value',
}
proc.path_fn = {
    '46 - Share of female police officers_data.csv': proc.proportion1,
}


for path, fn in proc.path_fn.items():

    in_path = os.path.join(proc.read_path, path)

    # read data frame
    df = pd.read_csv(in_path, header=1, encoding='latin1')

    # rename columns and drop rest
    df = df.rename(columns=proc.rename)[proc.rename.values()]

    # create map value
    df['map_value'] = df.value.apply(fn)

    # filter pays
    df = df[df['pays'].apply(lambda x: x not in proc.filter_country)]
    # translate pays
    df['pays'] = df['pays'].apply(lambda x: proc.country_dict_en2fr[x])
    # encode pays
    df['pays'] = df['pays'].apply(lambda x: proc.encode(x))

    # translate formulation
    df['formulation'] = df['formulation'].apply(
        lambda x: proc.form_dict_en2fr[x])
    # encode formulation
    df['formulation'] = df['formulation'].apply(lambda x: proc.encode(x))

    # save
    proc.to_csv(df, in_path)
