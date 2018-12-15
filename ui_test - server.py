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
        self.name : a name that is used at chatting (string)
        self.addr : address of server that receive my message(string)
        
        self.root : root of UI (tkinter.Tk)
        
        self.name_display : show name (tkinter.Label)
        self.address_display : show address (tkinter.Label)
        
        self.msg_log : chatting log (string)
        self.msg_log_label : it shows chatting log (tkinter.Label)

        self.renewal_button : renew log (tkinter.Button)
        
        self.input_msg_entry : input your msg (tkinter.Entry)
        self.send_btn : when this button is clicked, program sends a message (tkinter.Button)
        
        self.input_name_entry : input name (tkinter.Entry)
        self.set_name_btn : modify name (tkinter.Button)

        self.input_addr_entry : input address (tkinter.Entry)
        self.set_addr_btn : modify address (tkinter.Button)

        self.server_thread : thread for server (threading.Thread)

        self.renewal_log() ; renew log
        self.set_server() : set up server
            self.server_sock : socket for server (socket.socket)
        self.send_btn_clicked() : send message
        self.set_name() : set name
        self.set_addr() : set address
        --------------------------------------
        [name display]
        [address display]
        
        [chatting log]
        [renewal button]
        
        [input message entry]
        [send button]
        
        [input name entry]
        [set name button]
        
        [input address entry]
        [set address button]
        '''
        self.name = "Anonymous"
        self.addr = "127.0.0.1"
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


















