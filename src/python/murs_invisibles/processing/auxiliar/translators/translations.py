#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
from google.cloud import translate
import six

translate_client = translate.Client()

target = 'es'

with open('country_fr2fr.json', 'r', encoding='utf-8') as fp:
    country_fr2fr = json.load(fp, encoding='utf-8')

country_fr2es = {}
for c in country_fr2fr.keys():
    # Text can also be a sequence of strings, in which case this method
    # will return a sequence of results for each text.
    if isinstance(c, six.binary_type):
        c = c.decode('utf-8')
    result = translate_client.translate(c, target_language=target)
    country_fr2es[c] = result['translatedText']

print(country_fr2es)

with open('country_fr2es.json', 'w', encoding='utf-8') as fp:
    json.dump(country_fr2es, fp, indent=4)
