import os
import pandas as pd
from murs_invisibles.max_endecoding import (maxEncode, maxIntHackEncode)


class IO():

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

    @classmethod
    def encode_rows(cls, data_frame):
        """
        encode country and formulation
        """
        data_frame['year'] = data_frame['year'].apply(maxIntHackEncode)
        data_frame['country'] = data_frame['country'].apply(maxEncode)
        data_frame['indicator'] = data_frame['indicator'].apply(maxEncode)
        data_frame['value'] = data_frame['value'].apply(maxEncode)
        try:
            data_frame.year = data_frame.year.astype(int)
        except:
            pass
        return data_frame

    def _replace_source_folder(self, path):
        path = maxEncode(path)
        return path.replace('sources', f'm4l/{self.target_language}')

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
        print(df)
        print(df.sample(n=min(self.n_show, len(df))))
        print(f"{len(df)} entries")
        print(f"Saved at {out_path}\n")

    @classmethod
    def sort(cls, df):
        df.reset_index(drop=True, inplace=True)
        df = df.assign(ind_len=df.indicator.apply(len))
        return df.sort_values(by='ind_len', axis=0).drop('ind_len', axis=1)

    @classmethod
    def get_cuts(cls, df, props):
        cuts = [0]
        length = len(df)
        for p in props:
            cuts.append(cuts[-1] + int(p * length / sum(props)))
        return cuts

    def split_prop(self, props, df, path):
        df = self.sort(df)
        cuts = self.get_cuts(df, props)
        out_path = self.get_out_path(path)
        for c in range(len(cuts) - 1):
            this_out_path = out_path.split('.tsv', maxsplit=1)[0] + f"_{c}.tsv"
            tmp = df.iloc[cuts[c]:cuts[c + 1]]
            tmp.to_csv(
                this_out_path,
                index=False,
                header=False,
                encoding='utf-8',
                sep=self.out_sep)
            print(tmp.sample(n=min(self.n_show, len(tmp))))
            print(f"{len(tmp)} entries")
            print(f"Saved at {this_out_path}\n")

    def split(self, nb_outs, df, path):
        df = self.sort(df)
        batch_size = int(len(df) / nb_outs)
        out_path = self.get_out_path(path)
        for i in range(nb_outs):
            this_out_path = out_path.split('.tsv', maxsplit=1)[0] + f"_{i}.tsv"
            tmp = df.iloc[batch_size * i:batch_size * (i + 1)]
            tmp.to_csv(
                this_out_path,
                index=False,
                header=False,
                encoding='utf-8',
                sep=self.out_sep)
            print(tmp.sample(n=min(self.n_show, len(tmp))))
            print(f"{len(tmp)} entries")
            print(f"Saved at {this_out_path}\n")

    def split_prop_12(self, df, path):
        # save first the whole dataframe
        self.one_save(df, path)
        self.split_prop([1, 2], df, path)

    def split2(self, df, path):
        # save first the whole dataframe
        self.one_save(df, path)
        self.split(2, df, path)

    def split3(self, df, path):
        # save first the whole dataframe
        self.one_save(df, path)
        self.split(3, df, path)

    def split4(self, df, path):
        # save first the whole dataframe
        self.one_save(df, path)
        self.split(4, df, path)

    def get_out_path_indicator(self, path, indicator):
        tmp_path = self._replace_source_folder(path)
        out_dir = os.path.dirname(tmp_path)
        indicator = indicator.replace('/', '_').replace(',', '_')
        out_path = os.path.join(out_dir, indicator + ".tsv")
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
            print(f"{tmp} entries")
            print(f"Saved at {out_path}\n")

    @classmethod
    def remove_nan(cls, df):
        nb = len(df)
        df = df.dropna(axis=0)
        nb_nan = len(df)
        if nb_nan < nb:
            print(f"/!/ Drop {nb - nb_nan} rows with NAN values /!/ ")
        return df

    def save(self, table, df, path):
        df = self.encode_rows(df)
        df = df[self.out_values]
        df = self.remove_nan(df)
        getattr(self, self.save_fns[table])(df, path)
        return df
