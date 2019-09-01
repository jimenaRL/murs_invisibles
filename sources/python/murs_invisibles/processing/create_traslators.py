import os
import json
from pprint import pprint
import pandas as pd
from glob import glob
from pathlib import Path


# indicateor_fr2fr = "/Users/jimenarl/Desktop/git_murs/sources/python/murs_invisibles/processing/aux/translators/indicator_fr2fr.json"

BASE_FOLDER = "/Users/jimenarl/Desktop/git_murs/data/sources/"


FOLDERS = [
    "CNC-Audiens/audiens",
    "CNC-Audiens/cnc1",
    "CNC-Audiens/cnc2",
    "CNC-Audiens/audiens/tout",
    "EESR/EESR-FR",
    "EESR/parite2019",
    "INSEE",
    "MINIST-CULT",
    "canada",
    "oecd/developpement",
    "oecd/education",
    "oecd/emploi",
    "oecd/entrepreneuriat",
    "oecd/gouvernance",
    "onu/dataunorg",
    "onu/genderstats",
    "secretariat_egalite_femmes_hommes",
    "secretariat_egalite_femmes_hommes_2",
]


for folder in FOLDERS:
    print(folder)
    dicco_path = os.path.join(folder, 'indicator_v.json')
    print(dicco_path)
    for filename in Path(os.path.join(BASE_FOLDER, folder)).glob('*.csv'):
        print(filename)
        df = pd.read_csv(filename, encoding='utf-8')
        print(df.columns.tolist())
        # dicco = {i: "" for i in df.nom.tolist()}
        # pprint(dicco)

exit()

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
