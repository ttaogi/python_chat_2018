import sys
import socket
from threading import *


_NAME = ""
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
        #addr = socket.getaddrinfo("127.0.0.1", listening_port, socket.AF_INET, socket.SOCK_DGRAM)[0]
        #sock.bind(addr[4])
        sock.bind(("", _SERVER_PORT))
    except Exception as e:
        if sock:
            sock.close()
        print(":::server_mode getaddrinfo() of bind() error.\n")
        print(e)
        sys.exit(1)

    #try:
    #    sock.listen(_LISTEN_COUNT)
    #except Exception as e:
    #    if sock:
    #        sock.close()
    #    print(":::server_mode listen() error.\n")
    #    print(e)
    #    sys.exit(1)

    while True:
        try:
            #try:
            #    sender, sender_addr = sock.accept()
            #except Exception as e:
            #    if sender:
            #        sender.close()
            #    print(":::server_mode accept() error.\n")
            #    print(e)
            #    continue

            try:
                #msg = ""
                #while True:
                #    tmp = sender.recv(_BUFFER_SIZE)
                #    if len(tmp) > 0:
                #        msg = msg + tmp
                #    else
                #        break
                msg = sock.recv(_BUFFER_SIZE)
            except Exception as e:
                #if sender:
                #    sender.close()
                print(":::server_mode recv() error.\n")
                print(e)
                continue

            if msg.decode("utf-8").find("/quit") != -1:
                print("Terminating connection.\n")
                break
                
            print(">>> ", msg.decode("utf-8"))

            #sender.close()
        except Exception as e:
            if sock:
                sock.close()
            #if sender:
            #    sender.close()
            print(":::server_mode while error.\n")
            print(e)
            sys.exit(1)

    if sock:
        sock.close()


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
            msg = input("Input msg : ")
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

while True:
    print("[1] : server mode\n[2] : client mode\n[3] : quit\n")
    command = input("Select mode : ")
    
    if command == '1':
        server_thread = Thread(target=server_mode, args=())
        server_thread.start()
        break
    elif command == '2':
        _NAME = input("Input your name : ")
        client_thread = Thread(target=client_mode, args=())
        client_thread.start()
        break
    elif command == '3':
        print("Terminating chat.\n")
        sys.exit(1)
    else:
        print("Wrong input.\n")
        print("Please input again.\n\n")











