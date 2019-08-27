import sys
import time
import socket
import random
import argparse

from osc import decodeOSC
from murs_invisibles.max_endecoding import maxDecode

EXPECTED_DECODED_LENGTH = 6
CLEAN = 100


def add_line_breaks(out, indent):

    indent = ' ' * indent

    words = []
    for w in out.split(' '):
        words.extend([w, ' '])
    words = words[:-1]
    is_space = list(map(lambda c: c == ' ', words))
    words_lengths = list(map(len, words))

    current_nb_char = 0
    for i in range(len(words)):
        word = words[i]
        current_nb_char += words_lengths[i]
        if word == ' ':
            if current_nb_char + words_lengths[i+1] > max_char:
                words[i] = '\n' + indent
                current_nb_char = 0
    words[0] = indent + words[0]
    out = ''.join(words)
    ### HOT FIX ###
    out = out.replace('part\ndes femmes', '\n'+'part des femmes')
    out = out.replace('part des\nfemmes', '\n'+'part des femmes')
    ### ### ###  ###

    return out


def remove_dash(word):
    return word.replace(' - ', ' ')


if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument('-dry',
                        dest='dry',
                        default=False,
                        action='store_true')
    # parser.add_argument('-linebreak',
    #                     dest='linebreak',
    #                     default=False,
    #                     action='store_true')
    parser.add_argument('-ip',
                        dest='UDP_IP',
                        type=str,
                        default="localhost")
    parser.add_argument('-port',
                        dest="UDP_PORT",
                        type=int,
                        default=9000)
    parser.add_argument('-indent',
                        dest="indent",
                        type=int,
                        default=0)
    parser.add_argument('-in_line_breaks',
                        dest="in_line_breaks",
                        type=int,
                        default=0)
    parser.add_argument('-out_line_breaks',
                        dest="out_line_breaks",
                        type=int,
                        default=0)
    parser.add_argument('-max_char',
                        dest="max_char",
                        type=int,
                        default=16)

    for k, v in parser.parse_args().__dict__.items():
        locals()[k] = v

    # clear window
    for i in range(300):
        print('\n')

    # if dry do nothing
    if dry:
        while True:
            time.sleep(300)

    # set udp server
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((UDP_IP, UDP_PORT))

    nb_errors = 0
    while True:
        decoded = decodeOSC(sock.recv(1024))
        if not len(decoded) == EXPECTED_DECODED_LENGTH:
            nb_errors += 1
            print("Error number %i: len(decoded) is %i, expected %i." % (
                nb_errors,
                len(decoded),
                EXPECTED_DECODED_LENGTH))
            continue
        endpoint, _ = decoded[:2]
        # print
        if endpoint == "/woman":
            country, year, measure, value = map(maxDecode, decoded[2:])
            measure = remove_dash(measure)
            out = "%s %s %s %s" % (country, year, measure, value)
            out = add_line_breaks(out, indent)
            out = '\n' * in_line_breaks + out
            out = out + '\n' * out_line_breaks
            print(out)
        # clear window
        elif endpoint == "/clean":
            print('\n' * CLEAN)
        else:
            print(
                "Wrong endpoint %s. Must be '/woman' or '/clean'." % endpoint)
            continue
