import pandas as pd


class PostProcesser(object):

    def __init__(self, config):
        """
        Config example:
            {
                'fns': 'postprocess_fn',
            }
        """

        self.fns = config['fns']

    @classmethod
    def diff_perc(cls, df):
        df['sign'] = df.apply(
            lambda row: '+' if row.value >= 0 else '-', axis=1)
        df['value'] = df.apply(
            lambda row: row.sign + '%1.2f' % abs(row.value) + '%', axis=1)
        return df

    @classmethod
    def conditions_de_vie(cls, df):
        df['sign'] = df.apply(
            lambda row: '+' if row.value >= 0 else '-', axis=1)
        df['value'] = df.apply(
            lambda row: row.sign + '%i' % abs(row.value) + ' minutes', axis=1)
        return df

    @classmethod
    def percX100(cls, df):
        df['value'] = df.apply(
            lambda row: '%1.0f' % abs(100*row.value) + '%', axis=1)
        return df

    @classmethod
    def ratio(cls, df):
        df['value'] = df.apply(
            lambda row: row.value / (1 + row.value), axis=1)
        df['value'] = df.apply(
            lambda row: '%1.2f' % abs(row.value) + '%', axis=1)
        return df

    @classmethod
    def perc(cls, df):
        df['value'] = df.apply(
            lambda row: '%1.0f' % abs(row.value) + '%', axis=1)
        return df

    @classmethod
    def no_process(cls, df):
        return df

    def process(self, table, df):
        return getattr(self, self.fns[table])(df)
