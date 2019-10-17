import os
import unittest
import pandas as pd

DATA_FOLDER_PATH = os.path.join(
    os.path.dirname(os.path.realpath(__file__)), 'test_data')


from murs_invisibles.processing.pre_processer import PreProcesser


class PreprocessorTest(unittest.TestCase):

    table = "test_indicators.csv"
    config = {
        'fns': {
            table: ["remove_prop", "fsurtotal"]
        },
        'rename': {
            'country': 'pays',
            'year': 'annee',
            'indicator': 'nom',
            'value': 'part de femmes',
        },
    }

    df = pd.read_csv(os.path.join(DATA_FOLDER_PATH, "test_indicators.csv"))

    def test_load_config(self):
        self.preprocesser = PreProcesser(self.config)

    def test_preprocess(self):
        df = self.preprocesser.process(self.table, self.df)
        self.assertEqual(df.value.tolist()[0], 0.25)


if __name__ == '__main__':
    unittest.main()