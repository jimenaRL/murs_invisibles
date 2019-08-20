import pandas as pd
import json
from glob import glob

# indicateor_fr2fr = "/Users/jimenarl/Desktop/git_murs/sources/python/murs_invisibles/processing/aux/translators/indicator_fr2fr.json"


folders = [
    "/Users/jimenarl/Desktop/git_murs/data/sources/MINIST-CULT/*.csv",
]



# with open(indicateor_fr2fr, 'r', encoding='utf-8') as fp:
#     country_dict = json.load(fp)
# print(len(country_dict))


all_indicateurs = set()
for folder in folders:
    print(folder)
    paths = glob(folder)
    for p in paths:
        df = pd.read_csv(p, encoding='utf-8')
        indicateurs = df.nom.tolist()
        # dicco.update({i: i for i in indicateurs})
        for i in indicateurs:
            all_indicateurs.add('    '+'"{}": "{}",'.format(i, i))

for i in all_indicateurs:
    print(i)

# country_dict.update(dicco)
# print(country_dict)

# with open(indicateor_fr2fr, 'w', encoding='utf-8') as fp:
#     json.dump(country_dict, fp, indent=4)
