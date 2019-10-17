"""
Tools for encode/decode string for Max 7 compatibility.
"""

import unidecode

DICO = {
    ",": "---",
    "'": "-**-",
    " ": "_",
}

INV_DICO = {
    "---": ",",
    "-**-": "'",
    "_": " ",
    "__": " ",
}


def maxEncode(s):
    for k, v in DICO.items():
        s = s.replace(k, v)
    return s


def maxDecode(s):
    s = str(s)
    for k, v in INV_DICO.items():
        s = s.replace(k, v)
    return s
