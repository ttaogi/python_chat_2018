import sys
import time
import socket
import tkinter
from threading import *


_NAME = ""
_MSG_LOG = ""
_SERVER_PORT = 40725
_CLIENT_PORT = 40180
_BUFFER_SIZE = 4096
_LISTEN_COUNT = 5


##########
def server_mode():
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    except Exceptionn as e:
        if sock:
            sock.close()
        print(":::server_mode socket() error.\n")
        print(e)
        sys.exit(1)

    try:
        sock.bind(("", _SERVER_PORT))
    except Exception as e:
        if sock:
            sock.close()
        print(":::server_mode getaddrinfo() of bind() error.\n")
        print(e)
        sys.exit(1)

    while True:
        try:
            try:
                msg = sock.recv(_BUFFER_SIZE)
            except Exception as e:
                print(":::server_mode recv() error.\n")
                print(e)
                continue

            if msg.decode("utf-8").find("/quit") != -1:
                print("Terminating connection.\n")
                break

            if len(msg) == 0:
                continue
            
            print(">>> " + msg.decode("utf-8") + "\n")
        except Exception as e:
            if sock:
                sock.close()
            
            print(":::server_mode while error.\n")
            print(e)
            sys.exit(1)

    if sock:
        sock.close()



##########

server_thread = Thread(target=server_mode, args=())
server_thread.start()
print("server start")





















