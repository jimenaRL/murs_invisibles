import os
import json
from glob import glob
from os.path import join
import pandas as pd

from murs_invisibles.max_endecoding import maxEncode

IND_PATH = join(os.path.dirname(os.path.realpath(__file__)),
                'indicator_{}.json')

COUNTRY_PATH = join(os.path.dirname(os.path.realpath(__file__)),
                    'country_{}.json')

FILTER_COUNTRY_PATH = join(os.path.dirname(os.path.realpath(__file__)),
                           'country_filter_{}.txt')


class Processer(object):

    def __init__(self,
                 header,
                 encoding,
                 read_path,
                 filter_indicator_path,
                 file_valuemap,
                 file_save,
                 rename,
                 file_preprocess,
                 file_postprocess,
                 file_min_year,
                 country_filter_lang,
                 country_lang,
                 indicator_lang):
        """
        read_path: str
            path to folder with data files
        filter_indicator_path: str
            path to filter with indicators to filter
        file_preprocess: dict
            dictionary {'filename': 'preprocess_fn'}
        file_postprocess: dict
            dictionary {'filename': 'postprocess_fn'}
        file_valuemap: dict
            dictionary {'filename': 'valuemap_fn'}
        file_save: dict
            dictionary {'filename': 'save_fn'}
        file_min_year: dict
            dictionary {'filename': 'min_year'}
        rename: dict
            dictionary {'new_columns_name': 'old_columns_name'}
        country_filter_lang: str
            country language filter (e.g.: 'fr')
        country_lang: str
            country language in2out (e.g.: 'en2fr')
        indicator_lang: str
            indicator language in2out (e.g.: 'fr2fr')
        """

        self.header = header
        self.encoding = encoding

        self.filter_country_path = FILTER_COUNTRY_PATH.format(
            country_filter_lang)
        self.ind_path = IND_PATH.format(indicator_lang)
        self.country_path = COUNTRY_PATH.format(country_lang)

        self.read_path = read_path

        self.file_valuemap = {
            k: getattr(self, v) for k, v in file_valuemap.items()}

        self.file_preprocess = {
            k: getattr(self, v) for k, v in file_preprocess.items()}

        self.file_postprocess = {
            k: getattr(self, v) for k, v in file_postprocess.items()}

        self.file_save = {
            k: getattr(self, v) for k, v in file_save.items()}

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
    def proportion1(cls, row):
        """
        row: pandas dataframe row
             row.value contains p = m/(m+w) proportion in [0, 1]
        | 0 <= p <= 1
        | Perfect egality iff abs(p - .5) = 0
        | Maximum inegality iff abs(p - .5) = .5
        """
        return abs(row.value - .5) / .5

    @classmethod
    def proportion100(cls, row):
        """
        row: pandas dataframe row
             row.value contains p = m/(m+w) proportion in [0, 100]
        | 0 <= p <= 100
        | Perfect egality iff abs(p - 50.) = 0
        | Maximum inegality iff abs(p - 50.) = 50
        """
        row.value = row.value / 100.
        return cls.proportion1(row)

    @classmethod
    def ecart100(cls, row):
        """
        row: pandas dataframe row
             row.value contains p = m-w where m (resp. women) is the ratio of
             men (res. women) among all men (resp. women)
        | -100 <= p <= 100
        | Perfect egality iff abs(p) = 0
        | Maximum inegality iff abs(p) = 100
        """
        return abs(row.value) / 100.

    def postprocess(self, df, name):
        return self.file_postprocess[name](df)

    # @classmethod
    # def norm_wm(cls, row):
    #     """
    #     """
    #     return abs(row.value/(row.Value_men+row.Value_women))

    def no_preprocess(self, df):
        return df

    def remove_prop(self, df):
        df = df[~df.value.isna()]
        df.value = df.value.apply(lambda s: float(s.replace('%', '')))
        return df

    def diff_wm(self, df):
        """
        Dataframe preprocessing
        """

        df = df[df.AGE == 'TOTAL']
        df = df[df.Unit == 'Pourcentage']

        hash_cols = set(df.columns.tolist())
        hash_cols -= set(['SEX', 'Sexe', 'Value'])

        df['hash'] = df.apply(
            lambda row: hash(
                ''.join([str(row[c]) for c in hash_cols])), axis=1)

        hash_count = df.groupby(by='hash').count().SEX \
            .to_frame().reset_index().rename({'SEX': 'hash_count'}, axis=1)
        valid_hash = hash_count[hash_count.hash_count == 2]

        df = pd.merge(df, valid_hash, how='inner', on=['hash'])

        # /!\  HOTFIX /!\
        if 'WOMEN' in df['SEX'].unique().tolist():
            women_df = df[df['SEX'] == 'WOMEN']
            men_df = df[df['SEX'] == 'MEN']
        elif 'GIRLS' in df['SEX'].unique().tolist():
            women_df = df[df['SEX'] == 'GIRLS']
            men_df = df[df['SEX'] == 'BOYS']
        else:
            raise ValueError(
                f"Didn't found `GIRLS` nor `WOMEN` in df['SEX']:\
                    {df['SEX'].unique}")
        # /!\  HOTFIX /!\

        # /!\  HOTFIX /!\
        merge_on = list(
            set(self.rename.keys()) - set(['Value']) | set(['hash']))
        # /!\  HOTFIX /!\

        df = pd.merge(women_df,
                      men_df,
                      how='inner',
                      on=merge_on,
                      suffixes=('_women', '_men'))

        # /!\  HOTFIX /!\
        df = df[df.Value_men + df.Value_women > 0]
        # /!\  HOTFIX /!\

        df['value'] = df.apply(
            lambda row: row.Value_women - row.Value_men, axis=1)

        return df

    @classmethod
    def ratio(cls, df):
        df['value'] = df.apply(
            lambda row: row.value / (1 + row.value), axis=1)
        df['value'] = df.apply(
            lambda row: '%1.2f' % abs(row.value) + '%', axis=1)
        return df

    @classmethod
    def diff_perc(cls, df):
        df['sign'] = df.apply(
            lambda row: '+' if row.value >= 0 else '-', axis=1)
        df['value'] = df.apply(
            lambda row: row.sign + '%1.2f' % abs(row.value) + '%', axis=1)
        return df

    @classmethod
    def perc(cls, df):
        df['value'] = df.apply(
            lambda row: '%1.2f' % abs(row.value) + '%', axis=1)
        return df

    @classmethod
    def percX100(cls, df):
        df['value'] = df.apply(
            lambda row: '%1.0f' % abs(100*row.value) + '%', axis=1)
        return df

    @classmethod
    def women2men_ratio(cls, row):
        """
        row: pandas dataframe row
             row.value contain r = w/r ratio

        | 0 <= w/(m+w) = r/(1+r) <= 1
        | Perfect egality iff w/(m+w) = .5
        | Maximum inegality iff  abs(w/(m+w) - .5) = .5
        """
        row.value = row.value / (1 + row.value)
        return cls.proportion1(row)

    def get_out_path(self, in_path):
        out_path = maxEncode(in_path). \
            replace('sources', 'm4l'). \
            replace('.csv', '_17avril2019_14h20.tsv')
        out_dir = os.path.dirname(out_path)
        if not os.path.exists(out_dir):
            os.makedirs(out_dir)
        return out_path

    def one_save(self, df, in_path):
        out_path = self.get_out_path(in_path)
        df = df[self.out_values]
        df.to_csv(out_path,
                  index=False,
                  header=False,
                  encoding='utf-8',
                  sep=self.out_sep)
        print(df.sample(n=2))
        print("{} entries".format(len(df)))
        print("Saved at {}\n".format(out_path))

    def get_out_path_indicator(self, in_path, indicator):
        tmp_path = maxEncode(in_path).replace('sources', 'm4l')
        out_dir = os.path.dirname(tmp_path)
        indicator = indicator.replace('/', '_').replace(',', '_')
        out_path = os.path.join(out_dir, indicator+"_17avril2019_14h20.tsv")
        if not os.path.exists(out_dir):
            os.makedirs(out_dir)
        return out_path

    def sep_save(self, df, in_path):
        df = df[self.out_values]
        for indicator in df.indicator.unique():
            out_path = self.get_out_path_indicator(in_path, indicator)
            tmp = df[df.indicator == indicator]
            tmp.to_csv(out_path,
                       index=False,
                       header=False,
                       encoding='utf-8',
                       sep=self.out_sep)
            print(tmp.sample(n=2))
            print("{} entries".format(len(tmp)))
            print("Saved at {}\n".format(out_path))

    def save(self, name, df, in_path):
        self.file_save[name](df, in_path)

    def format_columns(self, df):
        """
        rename columns and drop rest
        """
        return df.rename(columns=self.rename)

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

        df['map_value'] = df.apply(self.file_valuemap[name], axis=1)
        return df

    def preprocess(self, df, name):
        """
        create map value
        """
        return self.file_preprocess[name](df)

    def encode_rows(self, df):
        """
        encode country and formulation
        """
        df['country'] = df['country'].apply(
            lambda x: maxEncode(x))
        df['indicator'] = df['indicator'].apply(
            lambda x: maxEncode(x))
        return df

    def process(self):

        for name in self.file_valuemap.keys():

            in_path = os.path.join(self.read_path, name)

            # load
            df = self.load_df(in_path)

            # preprocess data
            df = self.preprocess(df, name)

            # format
            df = self.format_columns(df)

            # compute map value
            df = self.map_value(df, name)

            # year
            df = self.filter_year(df, name)

            # process country
            df = self.filter_country(df)
            df = self.translate_country(df)

            # process indicator
            df = self.filter_indicator(df)
            df = self.translate_indicator(df)

            # postprocess value
            df = self.postprocess(df, name)

            # encode
            df = self.encode_rows(df)

            # save
            self.save(name, df, in_path)
