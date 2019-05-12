import os
import json
import pandas as pd


COUNTRY_PATH = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    'country_{}.json')
IND_PATH = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    'indicator_{}.json')


class Translator(object):

    def __init__(self, config):
        """
        Config example:
            {
                'country_lang': 'en2fr',
                'indicator_lang':'en2fr',
            }
        """
        with open(COUNTRY_PATH.format(config['country_lang']), 'r',
                  encoding='utf-8') as fp:
            self.country_dict = json.load(fp, encoding='utf-8')

        with open(IND_PATH.format(config['indicator_lang']), 'r',
                  encoding='utf-8') as fp:
            self.ind_dict = json.load(fp, encoding='utf-8')

    def translate_country(self, df):
        """
        translate country
        """
        df['country'] = df['country'].apply(
            lambda x: self.country_dict[x])
        return df

    def translate_indicator(self, df):
        """
        translate or reformulate indicator
        """
        df['indicator'] = df['indicator'].apply(
            lambda x: self.ind_dict[x])
        return df

    def process(self, table, df):
        df = self.translate_indicator(df)
        df = self.translate_country(df)
        return df
