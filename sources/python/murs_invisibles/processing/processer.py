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


COUNTRY_PATH = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    'auxiliar/translators/country_{}.json')

class Processer(object):

    def __init__(self, config):
        """
        Config example:
            {
                "base_path": "path/to/folder/with/raw/data",
                "io": {
                    "header": 1,
                    "encoding": 'latin1',
                    "fns": {
                        'filename': 'save_fn'
                    },
                },
                "preprocesser": {
                    'fns': {
                        'filename': 'preprocess_fn'
                    },
                    'rename': {
                        'country': 'Unnamed: 1',
                        'year': 'Year',
                        'indicator': 'Series',
                        'value': 'Value'
                    },
                },
                "mapper": {
                    'fns': {
                        'filename': 'map_value_fn',
                    }
                },
                "filter": {
                    'filter_indicator_path': None,
                    'country_filter_lang': 'en',
                    'year': {
                        'filename': 'min_year_threshold'
                    }
                },
                "translator": {
                    'country_lang': 'en2fr',
                    'indicator_lang': 'en2fr',
                },
                "postprocesser": {
                    'fns': {
                        'filename': 'postprocess_fn'
                    }
                },
            }
        """

        self.config = config
        self.base_path = config['base_path']
        self.tables = config['io']['fns'].keys()

        self.io = IO(config['io'])
        self.preprocesser = PreProcesser(config['preprocesser'])

        if not "origin_language" in config['filter']:
            config['filter'].update({
                "origin_language": config["origin_language"]
                })
        self.filter = Filter(config['filter'])

        self.mapper = Mapper(config['mapper'])

        default_translation = '{}2{}'.format(
                config["origin_language"],
                config["target_language"])

        IND_PATH = os.path.join(
            os.path.dirname(os.path.realpath(__file__)),
            'auxiliar/translators/indicator_{}.json')

        if not "indicator" in config['translator']:
            config['translator'].update({
                "indicator": default_translation
            })
        config['translator'].update({
            # "ind_dict_path": IND_PATH.format(default_translation)

            "ind_dict_path": os.path.join(
                self.base_path,
                "indicator_translations.csv")
            })

        if not "country" in config['translator']:
            config['translator'].update({
                "country": default_translation
                })
        config['translator'].update({
                "country_dict_path": COUNTRY_PATH.format(default_translation)
                })

        self.translator = Translator(config['translator'])

        self.postprocesser = PostProcesser(config['postprocesser'])

        self.sorter = Sorter(config['sorter'])

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
