import os
import json
import unidecode
from glob import glob
from os.path import join
import pandas as pd


IND_PATH = join(os.path.dirname(os.path.realpath(__file__)),
                'indicator_{}2{}.json')

COUNTRY_PATH = join(os.path.dirname(os.path.realpath(__file__)),
                    'country_{}2{}.json')

FILTER_COUNTRY_PATH = join(os.path.dirname(os.path.realpath(__file__)),
                           'country_filter_{}.txt')


class Processer(object):

    def __init__(self,
                 header,
                 encoding,
                 read_path,
                 filter_indicator_path,
                 file_fn,
                 rename,
                 file_min_year,
                 lang_in,
                 lang_out):
        """
        read_path: str
            path to folder with data files
        filter_indicator_path: str
            path to filter with indicators to filter
        file_fn: dict
            dictionary {'filename': 'processing_fn'}
        file_min_year: dict
            dictionary {'filename': 'min_year'}
        rename: dict
            dictionary {'new_columns_name': 'old_columns_name'}
        lang_in: str
            languag in (e.g.: 'en')
        lang_out: str
            languag out (e.g.: 'fr')
        """

        self.header = header
        self.encoding = encoding

        self.filter_country_path = FILTER_COUNTRY_PATH.format(lang_in)
        self.ind_path = IND_PATH.format(lang_in, lang_out)
        self.country_path = COUNTRY_PATH.format(lang_in, lang_out)

        self.read_path = read_path

        self.file_fn = {k: getattr(self, v) for k, v in file_fn.items()}

        self.rename = {v: k for k, v in rename.items()}

        self.file_min_year = file_min_year

        self.out_sep = '\t'

        self.out_values = [
            "country",
            "year",
            "indicator",
            "value",
            "map_value"
        ]

        self.dico = {
            # ",": "---",
            # "'": "-**-",
            " ": "_",
        }

        self.revers_dico = {
            # "---": ",",
            # "-**-": "'",
            "_": " ",
            "__": " ",
        }

        if filter_indicator_path:
            with open(filter_indicator_path, 'r', encoding='utf-8') as fp:
                self.filter_indicators = [
                    _.replace('\n', '') for _ in fp.readlines()]
        else:
            self.filter_indicators = []

        with open(self.filter_country_path, 'r', encoding='utf-8') as fp:
            self.filter_countries = [
                _.replace('\n', '') for _ in fp.readlines()]

        with open(self.country_path, 'r', encoding='utf-8') as fp:
            self.country_dict = json.load(fp, encoding='utf-8')

        with open(self.ind_path, 'r', encoding='utf-8') as fp:
            self.ind_dict = json.load(fp, encoding='utf-8')


    @classmethod
    def proportion1(cls, p):
        return abs(p - .5) / .5

    @classmethod
    def proportion100(cls, p):
        """
        abs(p - 50.) / 50
        """
        return cls.proportion1(p / 100)

    @classmethod
    def women2men_ratio(cls, r):
        """
        0 <= m/(m+w) = 1/(1+r) <= 1
        Perfect egality if and only if m/(m+w)  = 0.5.
        """
        return cls.proportion1(1. / (1 + r))
        # return abs(.5 - r / (1 + r)) / .5

    # def uniencode(self, s):
    #     return unidecode.unidecode(self.replace(s))

    def decode(self, s):
        s = str(s)
        for k, v in self.revers_dico.iteritems():
            s = s.replace(k, v)
        return s

    def replace(self, s):
        for k, v in self.dico.items():
            s = s.replace(k, v)
        return s

    def encode(self, s):
        return self.replace(s)

    def get_out_path(self, in_path):
        out_path = self.encode(in_path). \
            replace('sources', 'm4l'). \
            replace('csv', 'tsv')
        out_dir = os.path.dirname(out_path)
        if not os.path.exists(out_dir):
            os.makedirs(out_dir)
        return out_path

    def to_csv(self, df, in_path):
        out_path = self.get_out_path(in_path)
        df.to_csv(out_path,
                  index=False,
                  header=False,
                  encoding='utf-8',
                  columns=self.out_values,
                  sep=self.out_sep)
        print(df.sample(n=2))
        print("{} entries".format(len(df)))
        print("Saved at {}\n".format(out_path))

    def format_columns(self, df):
        """
        rename columns and drop rest
        """
        return df.rename(columns=self.rename)[self.rename.values()]

    def load_df(self, in_path):
        """
        read data frame
        """
        return pd.read_csv(
            in_path,
            header=self.header,
            encoding=self.encoding)

    def filter_year(self, df, name):
        """
        filter year
        """
        return df[df['year'] >= self.file_min_year[name]]

    def filter_country(self, df):
        """
        filter country
        """
        return df[df['country'].apply(
            lambda x: x not in self.filter_countries)]

    def translate_country(self, df):
        """
        translate country
        """
        df['country'] = df['country'].apply(
            lambda x: self.country_dict[x])
        return df

    def filter_indicator(self, df):
        """
        filter indicator
        """
        return df[df['indicator'].apply(
            lambda x: x not in self.filter_indicators)]

    def translate_indicator(self, df):
        """
        translate or reformulate indicator
        """
        df['indicator'] = df['indicator'].apply(
            lambda x: self.ind_dict[x])
        return df

    def map_value(self, df, name):
        """
        create map value
        """
        df['map_value'] = df.value.apply(self.file_fn[name])
        return df

    def encode_rows(self, df):
        """
        encode country and formulation
        """
        df['country'] = df['country'].apply(
            lambda x: self.encode(x))
        df['indicator'] = df['indicator'].apply(
            lambda x: self.encode(x))
        return df

    def process(self):

        for name in self.file_fn.keys():

            in_path = os.path.join(self.read_path, name)

            # load
            df = self.load_df(in_path)

            # format
            df = self.format_columns(df)

            # map value
            df = self.map_value(df, name)

            # year
            df = self.filter_year(df, name)

            # process country
            df = self.filter_country(df)
            df = self.translate_country(df)

            # process indicator
            df = self.filter_indicator(df)
            df = self.translate_indicator(df)

            # encode
            df = self.encode_rows(df)

            # save
            self.to_csv(df, in_path)
