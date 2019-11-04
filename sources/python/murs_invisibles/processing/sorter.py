import pandas as pd


class Sorter(object):

    def __init__(self, config):
        """
        Config example:
            {
                'fns': 'postprocess_fn',
            }
        """

        self.fns = config['fns']

    @classmethod
    def date_country(cls, df):
        df = df.sort_values(['indicator', 'year', 'country'])
        return df

    @classmethod
    def country_date_indicator(cls, df):
        df = df.sort_values(['country', 'year', 'indicator'])
        return df

    @classmethod
    def none(cls, df):
        return df

    def process(self, table, df):
        return getattr(self, self.fns[table])(df)
