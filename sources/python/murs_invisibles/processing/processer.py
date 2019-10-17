import os
from copy import deepcopy
import pandas as pd

from murs_invisibles.processing.mapper import Mapper
from murs_invisibles.processing.inout import IO
from murs_invisibles.processing.pre_processer import PreProcesser
from murs_invisibles.processing.post_processer import PostProcesser
from murs_invisibles.processing.filter import Filter
from murs_invisibles.processing.translator import Translator
from murs_invisibles.processing.sorter import Sorter

TARGET_LANG_ENV_VAR = 'MURS_INVIBLES_TARGET_LANG'
VALID_LANGS = ['es', 'fr']

TRANSLATOR_COUNTRY_PATH = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    'auxiliar/translators/country_{}.json')

FILTER_COUNTRY_PATH = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    'auxiliar/filters/country_filter_{}.txt')


class Processer(object):

    def _set_filter_config(self, filter_config):
        if not "origin_language" in filter_config:
            filter_config.update({
                "origin_language": self.config["origin_language"]
                })
        filter_config.update({
                "filter_country_path": FILTER_COUNTRY_PATH.format(
                    self.config['origin_language'])
                })
        return filter_config

    def _set_translator_config(self, translator_config):

        if not "indicator" in translator_config:
            translator_config.update({
                "indicator": self.default_translation
            })
        translator_config.update({
            "ind_dict_path": os.path.join(
                self.base_path,
                "indicator_translations.csv")
            })

        if not "country" in translator_config:
            translator_config.update({
                "country": self.default_translation
                })
        translator_config.update({
                "country_dict_path": TRANSLATOR_COUNTRY_PATH.format(
                    self.default_translation)
                })

        return translator_config

    def _set_io_config(self, io_config):
        io_config["target_language"] = self.get_global_target_language()
        return io_config

    def get_global_target_language(self):
        if TARGET_LANG_ENV_VAR in os.environ.keys():
            target_lang = os.environ[TARGET_LANG_ENV_VAR]
            if target_lang in VALID_LANGS:
                return target_lang
            else:
                msg = f"{TARGET_LANG_ENV_VAR} environ variable must be one of: "
                msg += ' '.join([f"'{_}'" for _ in VALID_LANGS])
                msg += f", got '{target_lang}'."
                raise ValueError(msg)

        raise ValueError(f"Missing {TARGET_LANG_ENV_VAR} environ variable.")

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
        self.default_translation = '{}2{}'.format(
            config["origin_language"],
            self.get_global_target_language())

        self.preprocesser = PreProcesser(config['preprocesser'])

        config['filter'] = self._set_filter_config(config['filter'])
        self.filter = Filter(config['filter'])

        self.mapper = Mapper(config['mapper'])

        config['translator'] = self._set_translator_config(config['translator'])
        self.translator = Translator(config['translator'])

        self.postprocesser = PostProcesser(config['postprocesser'])

        self.sorter = Sorter(config['sorter'])

        io_config = self._set_io_config(config['io'])
        self.io = IO(io_config)

    def process(self):

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
            self.io.save(table, df, path)
