import sys
import time
import socket
from tkinter import *
from threading import *


_SERVER_PORT = 40725
_CLIENT_PORT = 40180
_BUFFER_SIZE = 4096
_LISTEN_COUNT = 5
_LIMIT_MSG_LOG = 100


##########
class UI_TOP:
    def __init__(self):
        '''
        self.msg_log : log of chatting (string)
        
        self.root : root of UI (tkinter.Tk)
        
        self.name_display : show name (tkinter.Label)
        self.address_display : show address (tkinter.Label)
        
        self.msg_log : chatting log (string)
        self.msg_log_label : it shows chatting log (tkinter.Label)

        self.server_thread : thread for server (threading.Thread)

        self.set_server() : set up server
            self.server_sock : socket for server (socket.socket)
        --------------------------------------
        [chatting log]
        '''
        self.msg_log = "This is message log.\n"

        ##server
        self.set_server()

        ##UI
        self.root = Tk()
        self.root.title("Chat Server")
        self.root.geometry("500x500+50+50")

        self.msg_log_label = Label(self.root, text = self.msg_log, background = "light gray", width = 40, height = 20)
        self.msg_log_label.pack()

        self.server_thread = Thread(target=self.recv, args=())
        self.server_thread.start()
        
        ##
        self.root.mainloop()

    def __del__(self):
        if self.server_sock:
            self.server_sock.close()

    def set_server(self):
        try:
            self.server_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            self.server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.server_sock.bind(("", _SERVER_PORT))
        except Exception as e:
            self.msg_log = self.msg_log + "set_server() error(1).\n" + str(e) + "\n"
            if len(self.msg_log) > _LIMIT_MSG_LOG:
                self.msg_log = self.msg_log[len(self.msg_log)-_LIMIT_MSG_LOG:len(self.msg_log)]
            self.msg_log_label["text"] = self.msg_log
            if self.server_sock:
                self.server_sock.close()
                sys.exit(1)

    def recv(self):
        while True:
            try:
                msg = self.server_sock.recv(_BUFFER_SIZE)
                msg = msg.decode("utf-8")

                if len(msg) > 0:
                    self.msg_log = self.msg_log + msg + "\n"
                    if len(self.msg_log) > _LIMIT_MSG_LOG:
                        self.msg_log = self.msg_log[len(self.msg_log)-_LIMIT_MSG_LOG:len(self.msg_log)-1]
                    self.msg_log_label["text"] = self.msg_log
            except Exception as e:
                print("recv() error.\n")
                print(e)


##########

root = UI_TOP()


















