import os
import json
import pandas as pd

FILTER_COUNTRY_PATH = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    'country_filter_{}.txt')


class Filter(object):

    def __init__(self, config):
        """
        Config example:
            {
                'table_min_year': {
                    'filename': 2010
                }
                'country_filter_lang': 'fr',
                'filter_indicator_path': None,
            }
        """

        self.years = config['year']
        self.filter_country_path = FILTER_COUNTRY_PATH.format(
            config['country_filter_lang'])

        if config['filter_indicator_path']:
            with open(config['filter_indicator_path'], 'r',
                      encoding='utf-8') as fp:
                self.filter_indicators = [
                    _.replace('\n', '') for _ in fp.readlines()]
        else:
            self.filter_indicators = []

        with open(self.filter_country_path, 'r', encoding='utf-8') as fp:
            self.filter_countries = [
                _.replace('\n', '') for _ in fp.readlines()]

    def filter_year(self, df, table):
        """
        filter year
        """
        return df[df['year'] >= self.years[table]]

    def filter_country(self, df):
        """
        filter country
        """
        return df[df['country'].apply(
            lambda x: x not in self.filter_countries)]

    def filter_indicator(self, df):
        """
        filter indicator
        """
        return df[df['indicator'].apply(
            lambda x: x not in self.filter_indicators)]

    def process(self, table, df):
        df = self.filter_year(df, table)
        df = self.filter_country(df)
        df = self.filter_indicator(df)
        return df
