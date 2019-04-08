import time
import socket
import random
import argparse

from osc import decodeOSC
from endecoding import decode

EXPECTED_DECODED_LENGTH = 6

if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument('-dry',
                        dest='dry',
                        default=False,
                        action='store_true')
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
    parser.add_argument('-clean',
                        dest="clean",
                        type=int,
                        default=600)
    parser.add_argument('-in_line_breaks',
                        dest="in_line_breaks",
                        type=int,
                        default=1)
    parser.add_argument('-out_line_breaks',
                        dest="out_line_breaks",
                        type=int,
                        default=1)

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
        if endpoint == "/woman":
            country, year, measure, value = map(decode, decoded[2:])
            out = '\n' * in_line_breaks
            out += '\t' * random.randint(0, indent)
            out += "%s %s %s %s" % (country, year, measure, value)
            out += '\n' * out_line_breaks
            print(out)
        # clear window
        elif endpoint == "/clean":
            print('\n' * clean)
        else:
            print("Wrong endpoint %s. Must be '/woman' or '/clean'." % endpoint)
            continue