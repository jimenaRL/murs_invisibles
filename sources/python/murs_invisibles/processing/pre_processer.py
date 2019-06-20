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
        df['value'] = df.value.apply(lambda row: float(row.replace(',', '.')))
        return df


    def diff_wm(self, df):
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
            set(self.rename.values()) - set(['value']) | set(['hash']))
        # /!\  HOTFIX /!\

        df = pd.merge(women_df,
                      men_df,
                      how='inner',
                      on=merge_on,
                      suffixes=('_women', '_men'))

        # # /!\  HOTFIX /!\
        # df = df[df.value_men + df.value_women > 0]
        # # /!\  HOTFIX /!\

        df['value'] = df.apply(
            lambda row: row.value_women - row.value_men, axis=1)

        return df

    def process(self, table, df):
        df = self.format_columns(df)
        return getattr(self, self.fns[table])(df)
