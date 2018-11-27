import sys
import socket

from osc import decodeOSC
from endecoding import decode


if __name__ == "__main__":

    UDP_IP = "localhost"
    UDP_PORT = int(sys.argv[1])

    sock = socket.socket(socket.AF_INET,  # Internet
                         socket.SOCK_DGRAM)  # UDP
    sock.bind((UDP_IP, UDP_PORT))

    # clear window
    for i in range(300):
        print('\n')

    nb_errors = 0
    while True:
        decoded = decodeOSC(sock.recv(1024))
        if not len(decoded) == 6:
            nb_errors += 1
            print("Error number %i, len(decoded) is not 6.\n" % nb_errors)
            continue
        endpoint, _ = decoded[:2]
        if endpoint == "/woman":
            country, year, measure, value = map(decode, decoded[2:])
            print("%s %s %s %s" % (country, year, measure, value) + '\n')
        # clear window
        elif endpoint == "/clean":
            for i in range(600):
                print('\n')
        else:
            print("Wrong endpoint %s. Must be '/woman' or '/clean'.")
            continue
