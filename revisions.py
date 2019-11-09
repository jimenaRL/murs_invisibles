import os
import json
import pandas as pd
from murs_invisibles.max_endecoding import maxDecode


file_dir = os.path.dirname(os.path.realpath(__file__))
BASE_PATH = os.path.join(file_dir, "data/m4l/fr")

OUT_PATH = os.path.join(file_dir, "revisions")

def export(datas, name):
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

	with open(os.path.join(OUT_PATH, f'{name}.txt'), 'w') as f:
		f.writelines(out)
	print(out)


# tableau trash

tableau_trash = [
	"onu/genderstats/13_-_Gender_gap_in_wages__by_occupation__age_and_persons_with_disabilities_data.tsv",
	"onu/genderstats/1a_-_Average_number_of_hours_spent_on_domestic_chores_and_care_work__by_sex__age_and_location_data_0.tsv",
	"onu/genderstats/1a_-_Average_number_of_hours_spent_on_domestic_chores_and_care_work__by_sex__age_and_location_data_1.tsv",
	"INSEE/Conditions_de_vie_2015_-_temps_sociaux.tsv",
	"INSEE/Conditions_de_vie_Société_0.tsv",
	"INSEE/Conditions_de_vie_Société_1.tsv",
	"INSEE-95/INSEE-95_-_accès_à_l*emploi.tsv",
	"INSEE-95/INSEE-95_-_conseils_municipaux.tsv",
	"INSEE-95/INSEE-95_-_dossier_complet_val_d*oise_-_ecart.tsv",
	"INSEE-95/INSEE-95_-_dossier_complet_val_d*oise_-_pourcentage.tsv",
	"INSEE-95/INSEE-95_-_part_des_cadres.tsv",
	"INSEE-95/INSEE-95_-_taux_d*emploi.tsv",
	"INSEE-95/INSEE-95_-_taux_de_temps_partiel.tsv",
	"INSEE-95/INSEE-95_-_temps_partiel.tsv",
	"EESR/parite2019/parite2019_femmes-hommes.tsv",
	#
	"oecd/gouvernance/Cour_suprême=_ou_plus_haute_juridiction=_part_de_femmes.tsv",
	"oecd/developpement/GIDDB2014_titres_fonciers.tsv",
	"oecd/emploi/Part-de-l*emploi-dans-les-services-par-sexe.tsv",
	"oecd/emploi/Part-de-l*emploi-dans-les-services-par-sexe.tsv",
	"oecd/emploi/Part-de-l*emploi-dans-l*industrie-par-sexe.tsv",
	"oecd/emploi/Part-de-l*emploi-dans-l*agriculture-par-sexe-.tsv",
	"oecd/entrepreneuriat/Travailleur·euses_à_leur_compte=_part_des_femmes_par_rapport_à_celle_des_hommes.tsv",
]

export(datas=tableau_trash, name='trash')

# tableau disparition

tableau_disparition = [
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




