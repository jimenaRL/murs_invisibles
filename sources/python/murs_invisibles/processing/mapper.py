import numpy as np


class Mapper():

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
    def abstanh(cls, row, factor=0.1):
        return np.tanh(factor * np.abs(row.value))

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
    def percRel100_30(cls, row):
        return abs(row.value) / 30.

    @classmethod
    def diff_fm_minutes(cls, row):
        return abs(row.value) / 180.

    def diffHFPROP(self, row):
        """
        row: pandas dataframe row
             row.value contains p = 100 * (m-w)/m.
             where m is men wage and w is women wage.
        | -1 <= p <= 1
        | Perfect egality iff abs(p) = 0
        | Maximum inegality iff abs(p) = 1
        """
        return abs(self.abstanh(row, factor=0.05))

    @classmethod
    def diffFH_1(cls, row):
        """
        row: pandas dataframe row
             row.value contains p = (m-w)/100.
             where m (resp. women) is the ratio of
             men (res. women) among all men (resp. women)
        | -1 <= p <= 1
        | Perfect egality iff abs(p) = 0
        | Maximum inegality iff abs(p) = 1
        """
        return abs(row.value)

    @classmethod
    def diffFH_100(cls, row):
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
    def diffFH_10(cls, row):
        return abs(row.value) / 10.

    @classmethod
    def diffFH_15(cls, row):
        return abs(row.value) / 15.

    @classmethod
    def diffFH_20(cls, row):
        return abs(row.value) / 20.

    @classmethod
    def diffFH_25(cls, row):
        return abs(row.value) / 25.

    @classmethod
    def diffFH_hours_1(cls, row):
        return abs(row.value) / 1.

    @classmethod
    def diffFH_hours_4(cls, row):
        return abs(row.value) / 4.

    @classmethod
    def diffFH_50(self, row):
        return abs(self.abstanh(row, factor=0.05))

    @classmethod
    def women2men_ratio(cls, row):
        """
        row: pandas dataframe row
             row.value contain r = w/m ratio

        | 0 <= w/(m+w) = r/(1+r) <= 1
        | Perfect egality <=> w = m <=> w/(m+w) = .5
        | Maximum inegality <=> abs(w/(m+w) - .5) = .5
        """
        row.value = row.value / (1 + row.value)
        return cls.proportion1(row)

    def process(self, table, df):
        """
        create map value
        """
        df['map_value'] = df.apply(getattr(self, self.fns[table]), axis=1)
        return df
