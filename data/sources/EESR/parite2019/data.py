import os
import json
import pandas as pd
from murs_invisibles import Processer


config = {
    "data_path": os.path.dirname(os.path.realpath(__file__)),
    "io": {
        "header": 0,
        "encoding": 'utf-8',
        "fns": {
            "insertion_professionnelle.csv": "one_save",
            "part_des_femmes_principales_formations_enseignement_supérieur_2018.csv": "one_save",
            "titre_ingénieur.csv": "one_save",
            "personnels_enseignants_titulaires.csv": "one_save",
            "taux_emploi_titulaire_licence.csv": "one_save",
            "distinction.csv": "one_save",
            "parite2019_femmes-hommes.csv": "one_save",
            "parite2019_part_des_femmes.csv": "one_save",
        },
    },
    "preprocesser": {
        'fns': {
            "insertion_professionnelle.csv": "diff_fh",
            "part_des_femmes_principales_formations_enseignement_supérieur_2018.csv": "no_process",
            "titre_ingénieur.csv": "no_process",
            "personnels_enseignants_titulaires.csv": "no_process",
            "taux_emploi_titulaire_licence.csv": "diff_fh",
            "distinction.csv": "no_process",
            "parite2019_femmes-hommes.csv": "diff_fh",
            "parite2019_part_des_femmes.csv": "no_process",

        },
        'rename': {
            'country': 'pays',
            'year': 'annee',
            'indicator': 'nom',
            'value': 'part de femmes',
        },
    },
    "mapper": {
        'fns': {
            "insertion_professionnelle.csv": "ecart100",
            "part_des_femmes_principales_formations_enseignement_supérieur_2018.csv": "proportion100",
            "titre_ingénieur.csv": "proportion100",
            "personnels_enseignants_titulaires.csv": "proportion100",
            "taux_emploi_titulaire_licence.csv": "ecart100",
            "distinction.csv": "proportion100",
            "parite2019_femmes-hommes.csv": "ecart100",
            "parite2019_part_des_femmes.csv": "proportion100",
        }
    },
    "filter": {
        'filter_indicator_path': None,
        'country_filter_lang': 'fr',
        'year': {
            "insertion_professionnelle.csv": 2010,
            "part_des_femmes_principales_formations_enseignement_supérieur_2018.csv": 2010,
            "titre_ingénieur.csv": 2010,
            "personnels_enseignants_titulaires.csv": 2010,
            "taux_emploi_titulaire_licence.csv": 2010,
            "distinction.csv": 2010,
            "parite2019_femmes-hommes.csv": 2010,
            "parite2019_part_des_femmes.csv": 2010,
        }
    },
    "translator": {
        'country_lang': 'fr2fr',
        'indicator_lang': 'fr2fr',
    },
    "postprocesser": {
        'fns': {
            "insertion_professionnelle.csv": "diff_perc",
            "part_des_femmes_principales_formations_enseignement_supérieur_2018.csv": "perc",
            "titre_ingénieur.csv": "perc",
            "personnels_enseignants_titulaires.csv": "perc",
            "taux_emploi_titulaire_licence.csv": "diff_perc",
            "distinction.csv": "perc",
            "parite2019_femmes-hommes.csv": "diff_perc",
            "parite2019_part_des_femmes.csv": "perc",

        }
    },
    "sorter": {
        'fns': {
            "insertion_professionnelle.csv": "none",
            "part_des_femmes_principales_formations_enseignement_supérieur_2018.csv": "none",
            "titre_ingénieur.csv": "none",
            "personnels_enseignants_titulaires.csv": "none",
            "taux_emploi_titulaire_licence.csv": "none",
            "distinction.csv": "none",
            "parite2019_femmes-hommes.csv": "none",
            "parite2019_part_des_femmes.csv": "none",
        }
    },
}

Processer(config).process()
