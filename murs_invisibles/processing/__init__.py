import os
import json
import unidecode
from glob import glob
from os.path import join
import pandas as pd


EN2FR_FORM_PATH = join(os.path.dirname(os.path.realpath(__file__)),
                       'formulation_en2fr.json')

EN2FR_COUNTRY_PATH = join(os.path.dirname(os.path.realpath(__file__)),
                          'pays_en2fr.json')

FILTER_COUNTRY_PATH = join(os.path.dirname(os.path.realpath(__file__)),
                           'country_filter.txt')


class Processer(object):

    def __init__(self, read_path, file_fn, rename):
        """
        read_path: str
            path to folder with data files
        file_fn: dict
            dictionary {'filename': 'processing_fn'}
        rename_cols: dict
            dictionary {'old_columns_name': 'new_columns_name'}
        """

        self.read_path = read_path
        self.file_fn = {k: getattr(self, v) for k, v in file_fn.items()}
        self.rename = rename

        self.out_sep = '\t'

        self.out_values = [
            "pays",
            "année",
            "formulation",
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

        with open(FILTER_COUNTRY_PATH, 'r', encoding='utf-8') as fp:
            self.filter_country = [_.replace('\n', '') for _ in fp.readlines()]

        with open(EN2FR_COUNTRY_PATH, 'r', encoding='utf-8') as fp:
            self.country_dict_en2fr = json.load(fp, encoding='utf-8')

        with open(EN2FR_FORM_PATH, 'r', encoding='utf-8') as fp:
            self.form_dict_en2fr = json.load(fp, encoding='utf-8')

    def uniencode(self, s):
        return unidecode.unidecode(self.replace(s))

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
        print(df.head(2))
        print(df.tail(2))
        print("Saved at {}".format(out_path))

    @classmethod
    def proportion100(cls, p):
        return abs(p - 50.) / 50

    @classmethod
    def proportion1(cls, p):
        return abs(p - .5) / .5

    @classmethod
    def girls2boys_ratio(cls, r):
        return abs(.5 - r / (1 + r)) / .5

    def process(self):
        raise NotImplementedError()
