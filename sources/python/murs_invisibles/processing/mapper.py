import pandas as pd


class Mapper(object):

    def __init__(self, config):
        """
        Config example:
            {
                'filename': 'preprocess_fn',
                'rename':  {'new_columns_name': 'old_columns_name'}
            }
        """

        self.fns = config['fns']

    @classmethod
    def proportion1(cls, row):
        """
        row: pandas dataframe row
             row.value contains p = m/(m+w) proportion in [0, 1]
        | 0 <= p <= 1
        | Perfect egality iff  p = .5
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
    def ecart1(cls, row):
        """
        row: pandas dataframe row
             row.value contains p = (m-w)/100. where m (resp. women) is the ratio of
             men (res. women) among all men (resp. women)
        | -1 <= p <= 1
        | Perfect egality iff abs(p) = 0
        | Maximum inegality iff abs(p) = 1
        """
        return abs(row.value)

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

    @classmethod
    def ecart100_12(cls, row):
        return abs(row.value) / 12.

    @classmethod
    def ecart100_52(cls, row):
        return abs(row.value) / 52.

    @classmethod
    def women2men_ratio(cls, row):
        """
        row: pandas dataframe row
             row.value contain r = w/m ratio

        | 0 <= w/(m+w) = r/(1+r) <= 1
        | Perfect egality iff w/(m+w) = .5
        | Maximum inegality iff  abs(w/(m+w) - .5) = .5
        """
        row.value = row.value / (1 + row.value)
        return cls.proportion1(row)

    def process(self, table, df):
        """
        create map value
        """
        df['map_value'] = df.apply(getattr(self, self.fns[table]), axis=1)
        return df
