"""
Main data processer
"""

import os
import pandas as pd

from murs_invisibles.processing.mapper import Mapper
from murs_invisibles.processing.inout import IO
from murs_invisibles.processing.pre_processer import PreProcesser
from murs_invisibles.processing.post_processer import PostProcesser
from murs_invisibles.processing.filter import Filter
from murs_invisibles.processing.translator import Translator
from murs_invisibles.processing.sorter import Sorter

from murs_invisibles.processing.config import (
    VALID_LANGS,
    TARGET_LANG_ENV_VAR,
    TRANSLATOR_COUNTRY_PATH,
    FILTER_COUNTRY_PATH
)


class Processer():
    """
    Main data processer class.
    """

    def _set_filter_config(self, filter_config):
        if "origin_language" not in filter_config:
            filter_config.update({
                "origin_language": self.config["origin_language"]})
        filter_config.update({
            "filter_country_path": FILTER_COUNTRY_PATH.format(
                self.config['origin_language'])
        })
        return filter_config

    def _set_translator_config(self, translator_config):

        # set config to translate indicators
        if "indicator_origin_language" not in translator_config:
            indicator_translation = self.default_translation
        else:
            tcf = translator_config["indicator_origin_language"]
            gtl = self._get_global_target_language()
            indicator_translation = f'{tcf}2{gtl}'
        translator_config.update({"indicator": indicator_translation})
        translator_config.update({
            "ind_dict_path": os.path.join(
                self.base_path,
                "indicator_translations.csv")
        })

        # set config to translate countries
        if "country_origin_language" not in translator_config:
            country_translation = self.default_translation
        else:
            trc = translator_config["country_origin_language"]
            gtl = self._get_global_target_language()
            country_translation = f'{trc}2{gtl}'
        translator_config.update({"country": country_translation})
        translator_config.update({
            "country_dict_path": TRANSLATOR_COUNTRY_PATH.format(
                self.default_translation)
        })

        return translator_config

    def _set_io_config(self, io_config):
        io_config["target_language"] = self._get_global_target_language()
        return io_config

    @classmethod
    def _get_global_target_language(cls):
        if TARGET_LANG_ENV_VAR not in os.environ:
            raise ValueError(f"Missing {TARGET_LANG_ENV_VAR} env variable.")
        target_lang = os.environ[TARGET_LANG_ENV_VAR]
        if target_lang in VALID_LANGS:
            return target_lang
        msg = f"{TARGET_LANG_ENV_VAR} env variable must be one of: "
        msg += ' '.join([f"'{_}'" for _ in VALID_LANGS])
        msg += f", got '{target_lang}'."
        raise ValueError(msg)

    def __init__(self, config):
        """
        Config example:
            {
                "base_path": file_dir,
                "origin_language": "fr",
                "io": {
                    "header": 0,
                    "encoding": 'utf-8',
                    "fns": {
                        "taux.csv": "one_save",
                    },
                },
                "preprocesser": {
                    'fns': {
                        "taux.csv": "diffFH",
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
                        "taux.csv": "diffFH_100",
                    }
                },
                "filter": {
                    'filter_indicator_path': filter_indicator_path,
                    'year': {
                        "taux.csv": 2006,
                    }
                },
                "translator": {
                },
                "postprocesser": {
                    'fns': {
                        "taux.csv": "diff_perc",
                    }
                },
                "sorter": {
                    'fns': {
                        "taux.csv": "none",
                },
            }
        """

        self.config = config
        self.base_path = config['base_path']
        self.tables = config['io']['fns'].keys()
        ola = config["origin_language"]
        gtl = self._get_global_target_language()
        self.default_translation = f'{ola}2{gtl}'
        self.preprocesser = PreProcesser(config['preprocesser'])

        config['filter'] = self._set_filter_config(config['filter'])
        self.filter = Filter(config['filter'])

        self.mapper = Mapper(config['mapper'])

        config['translator'] = self._set_translator_config(
            config['translator']
        )
        self.translator = Translator(config['translator'])

        self.postprocesser = PostProcesser(config['postprocesser'])

        self.sorter = Sorter(config['sorter'])

        io_config = self._set_io_config(config['io'])
        self.io = IO(io_config)

    def process(self):
        """ Data pipeline."""

        out = {}
        for table in self.tables:

            print(f"***** {table} ****")
            path = os.path.join(self.base_path, table)

            # load
            df = self.io.load(path)
            # print(df.head())

            # preprocess
            df = self.preprocesser.process(table, df)
            # print(df.head())

            # filter
            df = self.filter.process(table, df)
            # print(df.head())

            # translate
            df = self.translator.process(table, df)
            # print(df.head())

            # compute map value
            df = self.mapper.process(table, df)
            # print(df.head())

            # postprocess
            df = self.postprocesser.process(table, df)
            # print(df.head())

            # sort
            df = self.sorter.process(table, df)

            # save
            df = self.io.save(table, df, path)

            # store df for postmerge
            out[table] = df

        # post merge
        if 'merge' in self.config:
            print("MERGED")
            for dicc in self.config['merge']:
                print(f">>>> {dicc['name']} <<<<")
                df_merged = pd.concat([out[data] for data in dicc["datas"]])
                df_merged = self.sorter.process(dicc["name"], df_merged)
                merged_path = self.io.get_out_path_indicator(
                    path, dicc['name'])
                self.io.one_save(df_merged, merged_path)
