import pandas as pd


class PreProcesser(object):

    def __init__(self, config):
        """
        Config example:
            {
                'filename': 'preprocess_fn',
                'rename':  {'new_columns_name': 'old_columns_name'}
            }
        """

        self.fns = config['fns']
        self.rename = {v: k for k, v in config['rename'].items()}

    def format_columns(self, df):
        """
        rename columns and drop rest
        """
        return df.rename(columns=self.rename)

    def remove_prop(self, df):
        df = df[~df.value.isna()]
        df.value = df.value.apply(lambda s: float(s.replace('%', '')))
        return df

    def no_process(self, df):
        return df

    def virg2point(self, df):
        values = ['value', 'femmes', 'hommes']
        for v in values:
            if v in df.columns:
                df[v] = df[v].apply(lambda row: float(row.replace(',', '.')))
        return df

    def remove_dollar_and_k(self, df):
        values = ['value', 'femmes', 'hommes']
        for v in values:
            if v in df.columns:
                df[v] = df[v].apply(lambda s: float(
                    s.replace(' k$', '').replace(',', '.').replace(' ', '')))
                df[v] = df[v].apply(lambda s: 1000.*float(s))
        return df

    def remove_euro_and_perc(self, df):
        values = ['value', 'femmes', 'hommes']
        for v in values:
            if v in df.columns:
                df[v] = df[v].apply(
                    lambda s: float(str(s).replace('€', '').replace('%', '')))
        return df


    def fsurtotal(self, df):
        df['value'] = df.femmes / (df.hommes+df.femmes)
        return df

    def perc_fsurtotal(self, df):
        df['value'] = 100. * df.femmes / (df.hommes+df.femmes)
        return df

    def virg2point_perc_fsurtotal(self, df):
        df = self.virg2point(df)
        df = self.perc_fsurtotal(df)
        return df

    def virg2point_diffFH(self, df):
        df = self.virg2point(df)
        df = self.diffFH(df)
        return df

    def diffFH(self, df):
        """
        Must be later in pp
        """
        df = self.remove_euro_and_perc(df)
        df['value'] = df.femmes-df.hommes
        return df

    def percRel1(self, df):
        """
        From Insee différence de salaires (F-H)/H (en %)
        https://drive.google.com/file/d/1iG7Zlq7eSL84n9bX-oROzYxK8GPhiMqA/view?usp=sharing
        """
        df['value'] = (df.femmes - df.hommes) / df.hommes
        return df

    def virg2point_percRel1(self, df):
        """
        """
        df = self.virg2point(df)
        df = self.percRel1(df)
        return df

    def virg2point_percRel100(self, df):
        """
        """
        df = self.virg2point(df)
        df = self.percRel100(df)
        return df

    def percRel100(self, df):
        """
        From Insee différence de salaires (F-H)/H (en %)
        https://drive.google.com/file/d/1iG7Zlq7eSL84n9bX-oROzYxK8GPhiMqA/view?usp=sharing
        """
        df['value'] = 100 * (df.femmes - df.hommes) / df.hommes
        return df

    def women2men(self, df):
        """
        """
        df['value'] = df.femmes / df.hommes
        return df

    def get_wm_then_percRel1(self, df):
        df = self.get_wm(df)
        df = self.percRel1(df)
        return df

    def get_wm_then_percRel100(self, df):
        df = self.get_wm(df)
        df = self.percRel100(df)
        return df

    def get_wm(self, df):
        """
        Dataframe preprocessing
        """

        df = df[df.AGE == 'TOTAL']
        df = df[df.Unit == 'Pourcentage']

        hash_cols = set(df.columns.tolist())
        hash_cols -= set(['SEX', 'Sexe', 'value'])

        df['hash'] = df.apply(
            lambda row: hash(
                ''.join([str(row[c]) for c in hash_cols])), axis=1)

        hash_count = df.groupby(by='hash').count().SEX \
            .to_frame().reset_index().rename({'SEX': 'hash_count'}, axis=1)
        valid_hash = hash_count[hash_count.hash_count == 2]

        df = pd.merge(df, valid_hash, how='inner', on=['hash'])

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

        merge_on = list(
            set(self.rename.values()) - set(['value']) | set(['hash']))

        df = pd.merge(women_df,
                      men_df,
                      how='inner',
                      on=merge_on,
                      suffixes=('_women', '_men'))

        merge_on.remove('hash')
        keep = merge_on + ['value_men', 'value_women']
        df = df[keep]

        df = df.rename(
            {'value_men': 'hommes', 'value_women': 'femmes'}, axis=1)

        return df

    def process(self, table, df):
        df = self.format_columns(df)
        return getattr(self, self.fns[table])(df)
