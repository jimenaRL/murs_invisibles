import os
import json
import pandas as pd
from murs_invisibles.max_endecoding import maxDecode


file_dir = os.path.dirname(os.path.realpath(__file__))
BASE_PATH = os.path.join(file_dir, "data/m4l/fr")

OUT_PATH = os.path.join(file_dir, "revisions")

# tableau disparition

datas = [
	"CNC-Audiens/tout/audiens_tout.tsv",
	"MINIST-CULT/OBS_GROUP4_TV.tsv",
	"oecd/developpement/GIDDB2019_poste_de_direction.tsv",
	"MINIST-CULT/Observatoire_group2_TH_.tsv",
	"CNC-Audiens/tout/tout_docs_1_part_des_femmes.tsv",
	"EESR/EESR-FR/all.tsv",
	"onu/dataunorg/SYB61_T05_Seats_held_by_Women_in_Parliament_0.tsv",
	"MINIST-CULT/OBS_GROUP3_arts.tsv",
	"secretariat_egalite_femmes_hommes/part_de_femmes.tsv",
	"onu/genderstats/43_-_Women’s_share_of_government_ministerial_positions_data_0.tsv",
]

datas_path = map(lambda s: os.path.join(BASE_PATH, s), datas)

out = ''
for p in datas_path:
	out += f'{p}\n'
	df = pd.read_csv(p, sep='\t',
		names=['country', 'year', 'indicator', 'value', 'map_value'])
	for c in ['country', 'year', 'indicator']:
		df[c] = df[c].apply(maxDecode)
	for i in df.indicator.unique():
		out += f'\t{i}\n'
#print(out)

with open(os.path.join(OUT_PATH, 'disparition.txt'), 'w') as f:
	f.writelines(out)


