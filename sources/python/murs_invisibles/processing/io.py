import os
import pandas as pd
from murs_invisibles.max_endecoding import maxEncode



class IO(object):

    def __init__(self, config):
        """
        Config example:
            {
                "header": 1,
                "encoding": 'latin1',
                "fns": {
                    'filename': 'save_fn'
                }
            }
        """

        self.save_fns = config['fns']

        self.header = config['header']
        self.encoding = config['encoding']

        self.out_sep = '\t'
        self.out_values = [
            "country",
            "year",
            "indicator",
            "value",
            "map_value"
        ]

    def load(self, path):
        """
        read data frame
        """
        return pd.read_csv(
            path,
            header=self.header,
            encoding=self.encoding)

    def encode_rows(self, df):
        """
        encode country and formulation
        """
        df['country'] = df['country'].apply(
            lambda x: maxEncode(x))
        df['indicator'] = df['indicator'].apply(
            lambda x: maxEncode(x))
        df.year = df.year.astype(int)
        return df

    def get_out_path(self, path):
        out_path = maxEncode(path). \
            replace('sources', 'm4l'). \
            replace('.csv', '.tsv')
        out_dir = os.path.dirname(out_path)
        if not os.path.exists(out_dir):
            os.makedirs(out_dir)
        return out_path

    def one_save(self, df, path):
        out_path = self.get_out_path(path)
        df = df[self.out_values]
        df.to_csv(out_path,
                  index=False,
                  header=False,
                  encoding='utf-8',
                  sep=self.out_sep)
        print(df.sample(n=2))
        print("{} entries".format(len(df)))
        print("Saved at {}\n".format(out_path))

    def get_out_path_indicator(self, path, indicator):
        tmp_path = maxEncode(path).replace('sources', 'm4l')
        out_dir = os.path.dirname(tmp_path)
        indicator = indicator.replace('/', '_').replace(',', '_')
        out_path = os.path.join(out_dir, indicator+".tsv")
        if not os.path.exists(out_dir):
            os.makedirs(out_dir)
        return out_path

    def sep_save(self, df, path):
        df = df[self.out_values]
        for indicator in df.indicator.unique():
            out_path = self.get_out_path_indicator(path, indicator)
            tmp = df[df.indicator == indicator]
            tmp.to_csv(out_path,
                       index=False,
                       header=False,
                       encoding='utf-8',
                       sep=self.out_sep)
            print(tmp.sample(n=2))
            print("{} entries".format(len(tmp)))
            print("Saved at {}\n".format(out_path))

    def save(self, table, df, path):
        df = self.encode_rows(df)
        getattr(self, self.save_fns[table])(df, path)
