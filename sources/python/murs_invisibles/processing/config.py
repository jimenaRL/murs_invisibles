import os

TRANSLATOR_COUNTRY_PATH = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    'auxiliar/translators/country_{}.json')

FILTER_COUNTRY_PATH = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    'auxiliar/filters/country_filter_{}.txt')

TARGET_LANG_ENV_VAR = 'MURS_INVIBLES_TARGET_LANG'
VALID_LANGS = ['es', 'fr']
