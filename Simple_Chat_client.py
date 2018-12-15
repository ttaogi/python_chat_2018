import sys
import time
import socket
import tkinter
from threading import *


_NAME = ""
_MSG_LOG = ""
_SERVER_PORT = 40725
_CLIENT_PORT = 40181
_BUFFER_SIZE = 4096
_LISTEN_COUNT = 5



##########
def client_mode():
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    except Exception as e:
        if sock:
            sock.close()
        print(":::client_mode socket() error.\n")
        print(e)
        sys.exit(1)

    try:
        sock.bind(("", _CLIENT_PORT))
    except Exception as e:
        if sock:
            sock.close()
        print(":::client_mode bind() error.\n")
        print(e)
        sys.exit(1)

    try:
        addr = input("Input target address : ")
        sock.connect((addr, _SERVER_PORT))
    except Exception as e:
        if sock:
            sock.close()
        print(":::client_mode connect() error.\n")
        print(e)
        sys.exit(1)

    while True:
        try:
            msg = input("Input msg : \n")
            if len(msg) == 0:
                continue
            else:
                sock.send((_NAME + " : " + msg).encode("utf-8"))
        except Exception as e:
            if sock:
                sock.close()
            print(":::client_mode send() error.\n")
            print(e)
            sys.exit(1)

        if msg.find("/quit") != -1:
            print("Terminating connection.\n")
            break

    sock.close()
        


##########

_NAME = input("Input name : ")

client_thread = Thread(target=client_mode, args=())
client_thread.start()
print("client start\n")





















