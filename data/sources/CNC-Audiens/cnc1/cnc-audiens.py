import os
import json
import pandas as pd
from murs_invisibles import Processer



config = {
    "base_path": os.path.dirname(os.path.realpath(__file__)),
    "origin_language": "fr",
    "io": {
        "header": 0,
        "encoding": 'utf-8',
        "fns": {
            "Effectifs_par_catégorie_professionnelle_ET_Répartition_des_effectifs_selon_l’année_d’agrément_et_le_sexe.csv": "one_save",
            "Films d’initiative française selon le genre des films et le sexe des réalisateur-trices.csv": "one_save",
            # "Part des entrées des films réalisés par des femmes.csv": "one_save",
            "Part des films réalisés par des femmes - Europe.csv": "one_save",
            # "Part des films réalisés par des femmes .csv": "one_save",
            # "Réalisateur·trices de courts métrages.csv": "one_save",
            # "écarts des salaires horaires médians des femmes et ceux des hommes dans le cinéma ciné.csv": "one_save",
        },
    },
    "preprocesser": {
        'fns': {
            "Effectifs_par_catégorie_professionnelle_ET_Répartition_des_effectifs_selon_l’année_d’agrément_et_le_sexe.csv": ["virg2point"],
            "Films d’initiative française selon le genre des films et le sexe des réalisateur-trices.csv": ["no_process"],
            # "Part des entrées des films réalisés par des femmes.csv": "diffFH",
            "Part des films réalisés par des femmes - Europe.csv": ["no_process"],
            # "Part des films réalisés par des femmes .csv": ["no_process"],
            # "Réalisateur·trices de courts métrages.csv": ["no_process"],
            "écarts des salaires horaires médians des femmes et ceux des hommes dans le cinéma ciné.csv": ["virg2point"],
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
            "Effectifs_par_catégorie_professionnelle_ET_Répartition_des_effectifs_selon_l’année_d’agrément_et_le_sexe.csv": "proportion100",
            "Films d’initiative française selon le genre des films et le sexe des réalisateur-trices.csv": "proportion100",
            # "Part des entrées des films réalisés par des femmes.csv": "",
            "Part des films réalisés par des femmes - Europe.csv": "proportion100",
            # "Part des films réalisés par des femmes .csv": "proportion100",
            # "Réalisateur·trices de courts métrages.csv": "",
            # "écarts des salaires horaires médians des femmes et ceux des hommes dans le cinéma ciné.csv": "",
        }
    },
    "filter": {
        'filter_indicator_path': None,
        'year': {
            "Effectifs_par_catégorie_professionnelle_ET_Répartition_des_effectifs_selon_l’année_d’agrément_et_le_sexe.csv": 2010,
            "Films d’initiative française selon le genre des films et le sexe des réalisateur-trices.csv": 2010,
            # "Part des entrées des films réalisés par des femmes.csv": 2010,
            "Part des films réalisés par des femmes - Europe.csv": 2010,
            # "Part des films réalisés par des femmes .csv": 2010,
            # "Réalisateur·trices de courts métrages.csv": 2010,
            # "écarts des salaires horaires médians des femmes et ceux des hommes dans le cinéma ciné.csv": 2010,
        }
    },
    "translator": {
    },
    "postprocesser": {
        'fns': {
            "Effectifs_par_catégorie_professionnelle_ET_Répartition_des_effectifs_selon_l’année_d’agrément_et_le_sexe.csv": "perc",
            "Films d’initiative française selon le genre des films et le sexe des réalisateur-trices.csv": "perc",
            # "Part des entrées des films réalisés par des femmes.csv": "",
            "Part des films réalisés par des femmes - Europe.csv": "perc",
            # "Part des films réalisés par des femmes .csv": "perc",
            # "Réalisateur·trices de courts métrages.csv": "",
            # "écarts des salaires horaires médians des femmes et ceux des hommes dans le cinéma ciné.csv": "",
        }
    },
    "sorter": {
        'fns': {
            "Effectifs_par_catégorie_professionnelle_ET_Répartition_des_effectifs_selon_l’année_d’agrément_et_le_sexe.csv": "none",
            "Films d’initiative française selon le genre des films et le sexe des réalisateur-trices.csv": "none",
            # "Part des entrées des films réalisés par des femmes.csv": "",
            "Part des films réalisés par des femmes - Europe.csv": "none",
            # "Part des films réalisés par des femmes .csv": "none",
            # "Réalisateur·trices de courts métrages.csv": "",
            # "écarts des salaires horaires médians des femmes et ceux des hommes dans le cinéma ciné.csv": "",
        }
    },
}

Processer(config).process()
