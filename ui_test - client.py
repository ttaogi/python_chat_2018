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

        ##UI
        self.root = Tk()
        self.root.title("Chat Client")
        self.root.geometry("500x500+50+50")

        self.name_display = Label(self.root, text = self.name, background = "light gray", width = 40, height = 1)
        self.name_display.pack()

        self.address_display = Label(self.root, text = self.addr, background = "light gray", width = 40, height = 1)
        self.address_display.pack()

        self.msg_log_label = Label(self.root, text = self.msg_log, background = "light gray", width = 40, height = 20)
        self.msg_log_label.pack()

        self.input_msg_entry = Entry(self.root, background = "light gray", width = 40)
        self.input_msg_entry.pack()

        self.send_btn = Button(self.root, text = "SEND")
        self.send_btn.bind("<Button-1>", self.send_btn_clicked)
        self.send_btn.pack()

        self.input_name_entry = Entry(self.root, background = "light gray", width = 20)
        self.input_name_entry.pack()

        self.set_name_btn = Button(self.root, text = "Input name")
        self.set_name_btn.bind("<Button-1>", self.set_name)
        self.set_name_btn.pack()

        self.input_addr_entry = Entry(self.root, background = "light gray", width = 20)
        self.input_addr_entry.pack()

        self.set_addr_btn = Button(self.root, text = "Input address")
        self.set_addr_btn.bind("<Button-1>", self.set_addr)
        self.set_addr_btn.pack()

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

    def send_btn_clicked(self, event):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            sock.bind(("", _CLIENT_PORT))
        except Exception as e:
            if sock:
                sock.close()
            self.msg_log = self.msg_log + "send_btn_clicked() error(1).\n" + str(e) + "\n"
            if len(self.msg_log) > _LIMIT_MSG_LOG:
                self.msg_log = self.msg_log[len(self.msg_log) - _LIMIT_MSG_LOG:len(self.msg_log)]
            self.msg_log_label["text"] = self.msg_log
            return

        try:
            sock.connect((self.addr, _SERVER_PORT))
            #
            msg = self.input_msg_entry.get()
            self.input_msg_entry.delete(0, END)
            #
            if len(msg) > 0:
                sock.send((self.name + " : " + msg).encode("utf-8"))
                self.msg_log = self.msg_log + self.name + " : " + msg + "\n"
                if len(self.msg_log) > _LIMIT_MSG_LOG:
                    self.msg_log = self.msg_log[len(self.msg_log) - _LIMIT_MSG_LOG:len(self.msg_log)]
                self.msg_log_label["text"] = self.msg_log
        except Exception as e:
            if sock:
                sock.close()
            self.msg_log = self.msg_log + "send_btn_clicked() error(2).\n" + str(e) + "\n"
            if len(self.msg_log) > _LIMIT_MSG_LOG:
                self.msg_log = self.msg_log[len(self.msg_log) - _LIMIT_MSG_LOG:len(self.msg_log)]
            self.msg_log_label["text"] = self.msg_log
            return

        sock.close()

    def set_name(self, event):
        name = self.input_name_entry.get()
        self.input_name_entry.delete(0, END)
        if len(name) > 0:
            self.name = name
        self.name_display["text"] = self.name

    def set_addr(self, event):
        addr = self.input_addr_entry.get()
        self.input_name_entry.delete(0, END)
        if len(addr) > 0:
            self.addr = addr
        self.address_display["text"] = self.addr

##########

root = UI_TOP()


















