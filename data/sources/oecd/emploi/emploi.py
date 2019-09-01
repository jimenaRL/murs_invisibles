import os
import json
import pandas as pd
from murs_invisibles import Processer

file_dir = os.path.dirname(os.path.realpath(__file__))
filter_indicator_path = os.path.join(file_dir, 'indicator_filter.txt')

config = {
    "base_path": file_dir,
    "origin_language": "fr",
    "target_language": "fr",
    "io": {
        "header": 0,
        "encoding": 'utf-8',
        "fns": {
            "Part-des-employés-à-temps-partiel-involontaire-par-sexe-et-groupe-d'âge.csv": "one_save",
            "Taux-d'activité-par-sexe-et-groupe-d'âge.csv": "one_save",
            # "Rapport-emploi-population-par-sexe-et-groupe-d’âge.csv": "one_save",
            "Part-des-employés-à-temps-partiel-par-sexe-et-groupe-d'âge.csv": "one_save",
            "Part-des-employés-temporaires-par-sexe.csv": "one_save",
            "Part-de-l'emploi-dans-l'agriculture-par-sexe-.csv": "one_save",
            "Part-de-l'emploi-dans-l'industrie-par-sexe.csv": "one_save",
            "Part-de-l'emploi-dans-les-services-par-sexe.csv": "one_save",
            # "Nombre-potentiel-d'années-à-la-retraite-par-sexe.csv": "one_save",
            # "Durée-du-congé-de-maternité.csv": "one_save",
            # "Durée-du-congé-parental-avec-protection-de-l'emploi.csv": "one_save",
           # "Durée-totale-du-congé-de-maternité-et-parental-payés.csv": "one_save",
            # "Durée-du-congé-payé-réservé-aux-pères.csv": "one_save",
            "Part-des-employés-cadres-supérieurs-par-sexe.csv": "one_save",
            # "Part-des-femmes-au-conseil-d'administration-des-plus-grandes-sociétés-cotées-en-bourse.csv": "one_save",
            "Taux-de-chômage-par-sexe-et-groupe-d'âge.csv": "one_save",
            # "Taux-d'emploi-équivalent-plein-temps-par-sexe.csv": "one_save",
        },
    },
    "preprocesser": {
        'fns': {
            "Part-des-employés-à-temps-partiel-involontaire-par-sexe-et-groupe-d'âge.csv": "diff_wm_insee_1",
            "Taux-d'activité-par-sexe-et-groupe-d'âge.csv": "diff_wm_insee_100",
            # "Rapport-emploi-population-par-sexe-et-groupe-d’âge.csv": "diff_wm_insee_100",
            "Part-des-employés-à-temps-partiel-par-sexe-et-groupe-d'âge.csv": "diff_wm_insee_100",
            "Part-des-employés-temporaires-par-sexe.csv": "diff_wm_insee_100",
            "Part-de-l'emploi-dans-l'agriculture-par-sexe-.csv": "diff_wm_insee_100",
            "Part-de-l'emploi-dans-l'industrie-par-sexe.csv": "diff_wm_insee_100",
            "Part-de-l'emploi-dans-les-services-par-sexe.csv": "diff_wm_insee_100",
            # "Nombre-potentiel-d'années-à-la-retraite-par-sexe.csv": "diff_wm_insee_100",
            # "Durée-du-congé-de-maternité.csv": "diff_wm_insee_100",
            # "Durée-du-congé-parental-avec-protection-de-l'emploi.csv": "diff_wm_insee_100",
           # "Durée-totale-du-congé-de-maternité-et-parental-payés.csv": "diff_wm_insee_100",
            # "Durée-du-congé-payé-réservé-aux-pères.csv": "diff_wm_insee_100",
            "Part-des-employés-cadres-supérieurs-par-sexe.csv": "diff_wm_insee_100",
            # "Part-des-femmes-au-conseil-d'administration-des-plus-grandes-sociétés-cotées-en-bourse.csv": "diff_wm_insee_100",
            "Taux-de-chômage-par-sexe-et-groupe-d'âge.csv": "diff_wm_insee_100",
            # "Taux-d'emploi-équivalent-plein-temps-par-sexe.csv": "diff_wm_insee_100",
        },
        'rename': {
            'country': 'Pays',
            'year': 'TIME',
            'indicator': 'Indicateur',
            'value': 'Value'
        },
    },
    "mapper": {
        'fns': {
            "Part-des-employés-à-temps-partiel-involontaire-par-sexe-et-groupe-d'âge.csv": "ecart1",
            "Taux-d'activité-par-sexe-et-groupe-d'âge.csv": "ecart100",
            # "Rapport-emploi-population-par-sexe-et-groupe-d’âge.csv": "ecart100",
            "Part-des-employés-à-temps-partiel-par-sexe-et-groupe-d'âge.csv": "ecart100",
            "Part-des-employés-temporaires-par-sexe.csv": "ecart100",
            "Part-de-l'emploi-dans-l'agriculture-par-sexe-.csv": "ecart100",
            "Part-de-l'emploi-dans-l'industrie-par-sexe.csv": "ecart100",
            "Part-de-l'emploi-dans-les-services-par-sexe.csv": "ecart100",
            # "Nombre-potentiel-d'années-à-la-retraite-par-sexe.csv": "ecart100",
            # "Durée-du-congé-de-maternité.csv": "ecart100",
            # "Durée-du-congé-parental-avec-protection-de-l'emploi.csv": "ecart100",
           # "Durée-totale-du-congé-de-maternité-et-parental-payés.csv": "ecart100",
            # "Durée-du-congé-payé-réservé-aux-pères.csv": "ecart100",
            "Part-des-employés-cadres-supérieurs-par-sexe.csv": "ecart100",
            # "Part-des-femmes-au-conseil-d'administration-des-plus-grandes-sociétés-cotées-en-bourse.csv": "ecart100",
            "Taux-de-chômage-par-sexe-et-groupe-d'âge.csv": "ecart100",
            # "Taux-d'emploi-équivalent-plein-temps-par-sexe.csv": "ecart100",
        }
    },
    "filter": {
        'filter_indicator_path': filter_indicator_path,
        'year': {
            "Part-des-employés-à-temps-partiel-involontaire-par-sexe-et-groupe-d'âge.csv": 2016,
            "Taux-d'activité-par-sexe-et-groupe-d'âge.csv": 2016,
            # "Rapport-emploi-population-par-sexe-et-groupe-d’âge.csv": 2016,
            "Part-des-employés-à-temps-partiel-par-sexe-et-groupe-d'âge.csv": 2016,
            "Part-des-employés-temporaires-par-sexe.csv": 2016,
            "Part-de-l'emploi-dans-l'agriculture-par-sexe-.csv": 2016,
            "Part-de-l'emploi-dans-l'industrie-par-sexe.csv": 2016,
            "Part-de-l'emploi-dans-les-services-par-sexe.csv": 2016,
            # "Nombre-potentiel-d'années-à-la-retraite-par-sexe.csv": 2016,
            # "Durée-du-congé-de-maternité.csv": 2016,
            # "Durée-du-congé-parental-avec-protection-de-l'emploi.csv": 2016,
           # "Durée-totale-du-congé-de-maternité-et-parental-payés.csv": 2016,
            # "Durée-du-congé-payé-réservé-aux-pères.csv": 2016,
            "Part-des-employés-cadres-supérieurs-par-sexe.csv": 2016,
            # "Part-des-femmes-au-conseil-d'administration-des-plus-grandes-sociétés-cotées-en-bourse.csv": 2016,
            "Taux-de-chômage-par-sexe-et-groupe-d'âge.csv": 2016,
            # "Taux-d'emploi-équivalent-plein-temps-par-sexe.csv": 2016,
        }
    },
    "translator": {
    },
    "postprocesser": {
        'fns': {
            "Part-des-employés-à-temps-partiel-involontaire-par-sexe-et-groupe-d'âge.csv": "diff_perc",
            "Taux-d'activité-par-sexe-et-groupe-d'âge.csv": "diff_perc",
            # "Rapport-emploi-population-par-sexe-et-groupe-d’âge.csv": "diff_perc",
            "Part-des-employés-à-temps-partiel-par-sexe-et-groupe-d'âge.csv": "diff_perc",
            "Part-des-employés-temporaires-par-sexe.csv": "diff_perc",
            "Part-de-l'emploi-dans-l'agriculture-par-sexe-.csv": "diff_perc",
            "Part-de-l'emploi-dans-l'industrie-par-sexe.csv": "diff_perc",
            "Part-de-l'emploi-dans-les-services-par-sexe.csv": "diff_perc",
            # "Nombre-potentiel-d'années-à-la-retraite-par-sexe.csv": "diff_perc",
            # "Durée-du-congé-de-maternité.csv": "diff_perc",
            # "Durée-du-congé-parental-avec-protection-de-l'emploi.csv": "diff_perc",
           # "Durée-totale-du-congé-de-maternité-et-parental-payés.csv": "diff_perc",
            # "Durée-du-congé-payé-réservé-aux-pères.csv": "diff_perc",
            "Part-des-employés-cadres-supérieurs-par-sexe.csv": "diff_perc",
            # "Part-des-femmes-au-conseil-d'administration-des-plus-grandes-sociétés-cotées-en-bourse.csv": "diff_perc",
            "Taux-de-chômage-par-sexe-et-groupe-d'âge.csv": "diff_perc",
            # "Taux-d'emploi-équivalent-plein-temps-par-sexe.csv": "diff_perc",
        }
    },
    "sorter": {
        'fns': {
            "Part-des-employés-à-temps-partiel-involontaire-par-sexe-et-groupe-d'âge.csv": "date_country",
            "Taux-d'activité-par-sexe-et-groupe-d'âge.csv": "date_country",
            # "Rapport-emploi-population-par-sexe-et-groupe-d’âge.csv": "date_country",
            "Part-des-employés-à-temps-partiel-par-sexe-et-groupe-d'âge.csv": "date_country",
            "Part-des-employés-temporaires-par-sexe.csv": "date_country",
            "Part-de-l'emploi-dans-l'agriculture-par-sexe-.csv": "date_country",
            "Part-de-l'emploi-dans-l'industrie-par-sexe.csv": "date_country",
            "Part-de-l'emploi-dans-les-services-par-sexe.csv": "date_country",
            # "Nombre-potentiel-d'années-à-la-retraite-par-sexe.csv": "date_country",
            # "Durée-du-congé-de-maternité.csv": "date_country",
            # "Durée-du-congé-parental-avec-protection-de-l'emploi.csv": "date_country",
           # "Durée-totale-du-congé-de-maternité-et-parental-payés.csv": "date_country",
            # "Durée-du-congé-payé-réservé-aux-pères.csv": "date_country",
            "Part-des-employés-cadres-supérieurs-par-sexe.csv": "date_country",
            # "Part-des-femmes-au-conseil-d'administration-des-plus-grandes-sociétés-cotées-en-bourse.csv": "date_country",
            "Taux-de-chômage-par-sexe-et-groupe-d'âge.csv": "date_country",
            # "Taux-d'emploi-équivalent-plein-temps-par-sexe.csv": "date_country",
        }
    },
}

Processer(config).process()
