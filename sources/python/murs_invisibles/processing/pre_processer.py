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
        self.values = ['value', 'femmes', 'hommes']

    def remove_google_sheet_nan(self, df):
        df = df[df.value != '#DIV/0!']
        df = df[df.value != '#VALUE!']
        return df

    def format_columns(self, df):
        """
        rename columns and drop rest
        """
        return df.rename(columns=self.rename)

    def remove_prop(self, df):
        for v in self.values:
            if v in df.columns:
                try:
                    df[v] = df[v].apply(lambda s: float(s.replace('%', '')))
                except Exception as e:
                    print("WARNING: unnable to remove '%' from {} columns: {}" \
                        .format(v, e))
        return df

    def no_process(self, df):
        return df

    def virg2point(self, df):
        for v in self.values:
            if v in df.columns:
                df[v] = df[v].apply(lambda row: row.replace(',', '.'))
        return df

    def remove_dollar_and_k(self, df):
        for v in self.values:
            if v in df.columns:
                df[v] = df[v].apply(lambda s: 
                    s.replace(' k$', '').replace(',', '.').replace(' ', ''))
                df[v] = df[v].apply(lambda s: 1000.*float(s))
        return df

    def remove_euro_and_perc(self, df):
        for v in self.values:
            if v in df.columns:
                df[v] = df[v].apply(
                    lambda s: str(s).replace('€', '').replace('%', ''))
        return df

    def x100(self, df):
        df['value'] = 100 * df['value']
        return df

    def fsurtotal(self, df):
        df['value'] = df.femmes / (df.hommes+df.femmes)
        return df

    def perc_fsurtotal(self, df):
        df['value'] = 100. * df.femmes / (df.hommes+df.femmes)
        return df

    def diffFH(self, df):
        """
        Units must be later in pp
        """
        df['value'] = df.femmes-df.hommes
        return df

    def percRel1(self, df):
        """
        From Insee différence de salaires (F-H)/H (en %)
        https://drive.google.com/file/d/1iG7Zlq7eSL84n9bX-oROzYxK8GPhiMqA/view?usp=sharing
        """
        df['value'] = (df.femmes - df.hommes) / df.hommes
        return df

    def percRel100(self, df):
        """
        From Insee différence de salaires (F-H)/H (en %)
        https://drive.google.com/file/d/1iG7Zlq7eSL84n9bX-oROzYxK8GPhiMqA/view?usp=sharing
        """
        df['value'] = 100 * (df.femmes - df.hommes) / df.hommes
        return df


    def get_wm_onu_gender_wages_gap(self, df):

        df.Occupation = df.Occupation
        df.indicator = df.indicator+ ' ' + df.Occupation
        df = df.drop('Occupation', axis=1)

        return self.get_wm_onu(df)



    def get_wm_onu_age(self, df):

        df.indicator = df.indicator+ ' ' + df.Age
        df = df.drop('Age', axis=1)

        return self.get_wm_onu(df)


    def get_wm_onu(self, df):

        if 'Location' in df and 'All areas' in df.Location.unique():
            df = df[df.Location == 'All areas']
        df = df[df.Sex != 'Both sexes']

        df = df.drop(['Location', 'Region', 'Occupation', 'LowerBound',
            'UpperBound', 'Unit', 'NatureData', 'OriginData', 'Country Code',
            'Footnote1', 'Footnote2', 'Footnote3', 'Footnote4', 'Footnote5',
            'Footnote6', 'Coverage'],
            axis=1, errors='ignore')

        hash_cols = set(df.columns.tolist())
        hash_cols -= set(['value', 'Sex'])

        df['hash'] = df.apply(
            lambda row: hash(
                ''.join([str(row[c]) for c in hash_cols])), axis=1)

        hash_count = df.groupby(by='hash').count().Sex \
            .to_frame().reset_index().rename({'Sex': 'hash_count'}, axis=1)
        valid_hash = hash_count[hash_count.hash_count == 2]

        df = pd.merge(df, valid_hash, how='inner', on=['hash'])

        women_df = df[df['Sex'] == 'Female']
        men_df = df[df['Sex'] == 'Male']

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


    def get_wm_oecd(self, df):
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

    def try_float_conversion(self, df):
        for v in self.values:
            if v in df.columns:
                try:
                    df[v] = df[v].apply(lambda s: float(s))
                except:
                    pass
        return df


    def process(self, table, df):
        df = self.format_columns(df)
        for fn in self.fns[table]:
            df = getattr(self, fn)(df)
            df = self.try_float_conversion(df)
        df = df[self.rename.values()]
        return df
