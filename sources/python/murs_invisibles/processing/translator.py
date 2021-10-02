import json
import pandas as pd


class Translator():

    def __init__(self, config):
        """
        Config example:
            {
                'indicator': 'en2fr',
                'country': 'fr2fr'
                'country_dict_path': ''
                'ind_dict_path': ''
            }
        """

        self.config = config

        self.origin_language = self.config['indicator'].split('2')[0]
        self.target_language = self.config['indicator'].split('2')[-1]

        with open(config['country_dict_path'], 'r', encoding='utf-8') as fp:
            self.country_dict = json.load(fp, encoding='utf-8')

        self.ind_dict = pd.read_csv(config['ind_dict_path'])
        # HOT FIX #
        self.ind_dict.drop_duplicates(inplace=True)

    def translate_country(self, df):
        """
        translate country
        """
        df['country'] = df['country'].apply(
            lambda x: self.country_dict[x])
        return df

    def translate_indicator(self, df):
        """
        translate or reformulate indicator
        """
        indicators = set(df.indicator.unique().tolist())
        avaliable_trads = set(self.ind_dict['indicator'].unique().tolist())
        missing_trads = indicators - avaliable_trads
        if missing_trads:
            print("Missing entries in translation dictionary.")
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            for i in missing_trads:
                print(f'"{i}","{i}",')
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            input("Press Enter to continue...")
        df = df.merge(self.ind_dict, on='indicator', how='inner')
        df['indicator'] = df[self.target_language]
        return df

    def process(self, table, df):
        df = self.translate_indicator(df)
        df = self.translate_country(df)
        return df
