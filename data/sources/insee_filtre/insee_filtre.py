import pandas as pd
from glob import glob

for p in glob("/Users/jimenarl/Desktop/chateau_ephemere_r2/murs_invisibles/data_tmp/m4l/insee_filtre/*/*.tsv"):
    df = pd.read_csv(p, sep='\t')
    df = df[df.year>=2014]
    print(df)
    df.to_csv(p, sep='\t', index=0, header=False)