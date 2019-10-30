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

        self.n_show = 10

        self.save_fns = config['fns']

        self.header = config['header']
        self.encoding = config['encoding']

        self.target_language = config["target_language"]

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
        try:
            df.year = df.year.astype(int)
        except:
            pass
        return df

    def _replace_source_folder(self, path):
        path = maxEncode(path)
        return path.replace('sources', 'm4l/{}'.format(self.target_language))


    def get_out_path(self, path):
        out_path = self._replace_source_folder(path).replace('.csv', '.tsv')
        out_dir = os.path.dirname(out_path)
        if not os.path.exists(out_dir):
            os.makedirs(out_dir)
        return out_path

    def one_save(self, df, path):
        out_path = self.get_out_path(path)
        df.to_csv(out_path,
                  index=False,
                  header=False,
                  encoding='utf-8',
                  sep=self.out_sep)
        print(df.sample(n=min(self.n_show, len(df))))
        print("{} entries".format(len(df)))
        print("Saved at {}\n".format(out_path))

    def split(self, n, df, path):
        df.reset_index(drop=True, inplace=True)
        batch_size = int(len(df) / n)
        out_path = self.get_out_path(path)
        for i in range(n):
            this_out_path = out_path.split('.tsv')[0] + "_{}.tsv".format(i)
            tmp = df.iloc[batch_size*i:batch_size*(i+1)]
            tmp.to_csv(this_out_path,
                      index=False,
                      header=False,
                      encoding='utf-8',
                      sep=self.out_sep)
            print(tmp.sample(n=min(self.n_show, len(tmp))))
            print("{} entries".format(len(tmp)))
            print("Saved at {}\n".format(this_out_path))


    def split2(self, df, path):
        self.split(2, df, path)

    def split3(self, df, path):
        self.split(3, df, path)

    def split4(self, df, path):
        self.split(4, df, path)

    def get_out_path_indicator(self, path, indicator):
        tmp_path = self._replace_source_folder(path)
        out_dir = os.path.dirname(tmp_path)
        indicator = indicator.replace('/', '_').replace(',', '_')
        out_path = os.path.join(out_dir, indicator+".tsv")
        if not os.path.exists(out_dir):
            os.makedirs(out_dir)
        return out_path

    def sep_save(self, df, path):
        for indicator in df.indicator.unique():
            out_path = self.get_out_path_indicator(path, indicator)
            tmp = df[df.indicator == indicator]
            tmp.to_csv(out_path,
                       index=False,
                       header=False,
                       encoding='utf-8',
                       sep=self.out_sep)
            print(tmp.sample(n=min(self.n_show, len(tmp))))
            print("{} entries".format(len(tmp)))
            print("Saved at {}\n".format(out_path))

    def remove_nan(self, df):
        nb = len(df)
        df = df.dropna(axis=0)
        nb_nan = len(df)
        if nb_nan < nb:
            print("/!\ Drop {} rows with NAN values /!\ ".format(
                nb - nb_nan))
        return df

    def save(self, table, df, path):
        df = self.encode_rows(df)
        df = df[self.out_values]
        df = self.remove_nan(df)
        getattr(self, self.save_fns[table])(df, path)
