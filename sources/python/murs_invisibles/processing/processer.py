import os

from murs_invisibles.processing.mapper import Mapper
from murs_invisibles.processing.io import IO
from murs_invisibles.processing.pre_processer import PreProcesser
from murs_invisibles.processing.post_processer import PostProcesser
from murs_invisibles.processing.filter import Filter
from murs_invisibles.processing.translator import Translator


class Processer(object):

    def __init__(self, config):
        """
        Config example:
            {
                "data_path": "path/to/folder/with/raw/data",
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

        self.data_path = config['data_path']
        self.tables = config['io']['fns'].keys()

        self.io = IO(config['io'])
        self.preprocesser = PreProcesser(config['preprocesser'])
        self.filter = Filter(config['filter'])
        self.mapper = Mapper(config['mapper'])
        self.translator = Translator(config['translator'])
        self.postprocesser = PostProcesser(config['postprocesser'])

    def process(self):

        for table in self.tables:

            print(f"***** {table} ****")
            path = os.path.join(self.data_path, table)

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

            # save
            self.io.save(table, df, path)
