import os
import json
import pandas as pd
from murs_invisibles import Processer

file_dir = os.path.dirname(os.path.realpath(__file__))
filter_indicator_path = os.path.join(file_dir, 'indicator_filter.txt')

config = {
    "base_path": file_dir,
    "origin_language": "es",
    "target_language": "es",
    "io": {
        "header": 0,
        "encoding": 'utf-8',
        "fns": {
            "Servicios -  Personal ocupado.csv": "one_save",
            "Mercado Laboral - Tiempo trabajo (horas a la semana).csv": "one_save",
            "Economía del cuidado - Valor económico del TDCNR según funcionalidad y sexo.csv": "one_save",
            "Mercado Laboral - Tasas desempleo - ocupación .csv": "one_save",
            "Pobreza de tiempo e ingreso - Pobreza.csv": "one_save",
            "Fuerza laboral y educacion - Poblacion activa.csv": "one_save",
            "Fuerza laboral y educacion -  Tasa de desempleo.csv": "one_save",
            "Economía del cuidado - Porcentaje de participación H_M en el TDCNR.csv": "one_save"
        },
    },
    "preprocesser": {
        'fns': {
            "Servicios -  Personal ocupado.csv": "virg2point",
            "Mercado Laboral - Tiempo trabajo (horas a la semana).csv": "virg2point_insee1",
            "Economía del cuidado - Valor económico del TDCNR según funcionalidad y sexo.csv": "virg2point_insee1",
            "Mercado Laboral - Tasas desempleo - ocupación .csv": "virg2point_insee1",
            "Pobreza de tiempo e ingreso - Pobreza.csv": "virg2point_insee1",
            "Fuerza laboral y educacion - Poblacion activa.csv": "virg2point_insee1",
            "Fuerza laboral y educacion -  Tasa de desempleo.csv": "virg2point_insee1",
            "Economía del cuidado - Porcentaje de participación H_M en el TDCNR.csv": "virg2point_insee1"
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
            "Servicios -  Personal ocupado.csv": "proportion100",
            "Mercado Laboral - Tiempo trabajo (horas a la semana).csv": "ecart100",
            "Economía del cuidado - Valor económico del TDCNR según funcionalidad y sexo.csv": "ecart100",
            "Mercado Laboral - Tasas desempleo - ocupación .csv": "ecart100",
            "Pobreza de tiempo e ingreso - Pobreza.csv": "ecart100",
            "Fuerza laboral y educacion - Poblacion activa.csv": "ecart100",
            "Fuerza laboral y educacion -  Tasa de desempleo.csv": "ecart100",
            "Economía del cuidado - Porcentaje de participación H_M en el TDCNR.csv": "ecart100"
        }
    },
    "filter": {
        'filter_indicator_path': filter_indicator_path,
        'year': {
            "Servicios -  Personal ocupado.csv": 2006,
            "Mercado Laboral - Tiempo trabajo (horas a la semana).csv": 2006,
            "Economía del cuidado - Valor económico del TDCNR según funcionalidad y sexo.csv": 2006,
            "Mercado Laboral - Tasas desempleo - ocupación .csv": 2006,
            "Pobreza de tiempo e ingreso - Pobreza.csv": 2006,
            "Fuerza laboral y educacion - Poblacion activa.csv": 2006,
            "Fuerza laboral y educacion -  Tasa de desempleo.csv": 2006,
            "Economía del cuidado - Porcentaje de participación H_M en el TDCNR.csv": 2006
        }
    },
    "translator": {
    },
    "postprocesser": {
        'fns': {
            "Servicios -  Personal ocupado.csv": "perc",
            "Mercado Laboral - Tiempo trabajo (horas a la semana).csv": "diff_perc",
            "Economía del cuidado - Valor económico del TDCNR según funcionalidad y sexo.csv": "diff_perc",
            "Mercado Laboral - Tasas desempleo - ocupación .csv": "diff_perc",
            "Pobreza de tiempo e ingreso - Pobreza.csv": "diff_perc",
            "Fuerza laboral y educacion - Poblacion activa.csv": "diff_perc",
            "Fuerza laboral y educacion -  Tasa de desempleo.csv": "diff_perc",
            "Economía del cuidado - Porcentaje de participación H_M en el TDCNR.csv": "diff_perc"
    }
    },
    "sorter": {
        'fns': {
            "Servicios -  Personal ocupado.csv": "none",
            "Mercado Laboral - Tiempo trabajo (horas a la semana).csv": "none",
            "Economía del cuidado - Valor económico del TDCNR según funcionalidad y sexo.csv": "none",
            "Mercado Laboral - Tasas desempleo - ocupación .csv": "none",
            "Pobreza de tiempo e ingreso - Pobreza.csv": "none",
            "Fuerza laboral y educacion - Poblacion activa.csv": "none",
            "Fuerza laboral y educacion -  Tasa de desempleo.csv": "none",
            "Economía del cuidado - Porcentaje de participación H_M en el TDCNR.csv": "none"
        }
    },
}

Processer(config).process()
