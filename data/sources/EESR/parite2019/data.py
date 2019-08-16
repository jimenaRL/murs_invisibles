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
            "parite2019 - Insertion professionnelle en 2017 des diplômés 2015 d’un Master de l’université.csv": "one_save",
            "parite2019 - Part des femmes dans les principales formations d'enseignement supérieur 2018.csv": "one_save",
            "parite2019 - Part des femmes diplômées d’un titre d’ingénieur de 2000 à 2017.csv": "one_save",
            "parite2019 - Personnels enseignants titulaires en activité dans l’enseignement supérieur - 2018.csv": "one_save",
            "parite2019 - Taux d’emploi des titulaires d’un diplôme de niveau Licence ou plus.csv": "one_save",
            "parite2019 - distinction  organismes publics de recherche.csv": "one_save",
            "parite2019_femmes-hommes.csv": "one_save",
            "parite2019_part_des_femmes.csv": "one_save",
        },
    },
    "preprocesser": {
        'fns': {
            "parite2019 - Insertion professionnelle en 2017 des diplômés 2015 d’un Master de l’université.csv": "diff_fh",
            "parite2019 - Part des femmes dans les principales formations d'enseignement supérieur 2018.csv": "no_process",
            "parite2019 - Part des femmes diplômées d’un titre d’ingénieur de 2000 à 2017.csv": "no_process",
            "parite2019 - Personnels enseignants titulaires en activité dans l’enseignement supérieur - 2018.csv": "no_process",
            "parite2019 - Taux d’emploi des titulaires d’un diplôme de niveau Licence ou plus.csv": "diff_fh",
            "parite2019 - distinction  organismes publics de recherche.csv": "no_process",
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
            "parite2019 - Insertion professionnelle en 2017 des diplômés 2015 d’un Master de l’université.csv": "ecart100",
            "parite2019 - Part des femmes dans les principales formations d'enseignement supérieur 2018.csv": "proportion100",
            "parite2019 - Part des femmes diplômées d’un titre d’ingénieur de 2000 à 2017.csv": "proportion100",
            "parite2019 - Personnels enseignants titulaires en activité dans l’enseignement supérieur - 2018.csv": "proportion100",
            "parite2019 - Taux d’emploi des titulaires d’un diplôme de niveau Licence ou plus.csv": "ecart100",
            "parite2019 - distinction  organismes publics de recherche.csv": "proportion100",
            "parite2019_femmes-hommes.csv": "ecart100",
            "parite2019_part_des_femmes.csv": "proportion100",
        }
    },
    "filter": {
        'filter_indicator_path': None,
        'country_filter_lang': 'fr',
        'year': {
            "parite2019 - Insertion professionnelle en 2017 des diplômés 2015 d’un Master de l’université.csv": 2010,
            "parite2019 - Part des femmes dans les principales formations d'enseignement supérieur 2018.csv": 2010,
            "parite2019 - Part des femmes diplômées d’un titre d’ingénieur de 2000 à 2017.csv": 2010,
            "parite2019 - Personnels enseignants titulaires en activité dans l’enseignement supérieur - 2018.csv": 2010,
            "parite2019 - Taux d’emploi des titulaires d’un diplôme de niveau Licence ou plus.csv": 2010,
            "parite2019 - distinction  organismes publics de recherche.csv": 2010,
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
            "parite2019 - Insertion professionnelle en 2017 des diplômés 2015 d’un Master de l’université.csv": "diff_perc",
            "parite2019 - Part des femmes dans les principales formations d'enseignement supérieur 2018.csv": "perc",
            "parite2019 - Part des femmes diplômées d’un titre d’ingénieur de 2000 à 2017.csv": "perc",
            "parite2019 - Personnels enseignants titulaires en activité dans l’enseignement supérieur - 2018.csv": "perc",
            "parite2019 - Taux d’emploi des titulaires d’un diplôme de niveau Licence ou plus.csv": "diff_perc",
            "parite2019 - distinction  organismes publics de recherche.csv": "perc",
            "parite2019_femmes-hommes.csv": "diff_perc",
            "parite2019_part_des_femmes.csv": "perc",

        }
    },
}

Processer(config).process()
