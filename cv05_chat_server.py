#! /usr/bin/env python3

from cv05_chat_protocol import Chat_proto, Ctrl_value
import socket as s

from threading import Thread

IP = "0.0.0.0"
PORT = 1111

def handle_client(client_sock : s.socket, chat_proto):
    while True:
        msg_bytes = client_sock.recv(1000)
        msg_text = msg_bytes.decode()

        (status, msg_type, data) = chat_proto.parse_proto_msg(msg_text)

        if (status == False):
            continue
        if (msg_type == Ctrl_value.LOGOUT.value):
            client_sock.close()
            return
        
        if (msg_type == Ctrl_value.USERS.value):
           msg_bytes = data.__str__().encode()
           client_sock.send(msg_bytes)
           continue


def chat_server():
    chat_proto = Chat_proto("server")
    #ip, tcp
    sock = s.socket(s.AF_INET, s.SOCK_STREAM)
    sock.bind((IP, PORT)) # bind ocakava jeden parameter - adresu - socket
    sock.listen(5)
    while True:
        (client_sock, client_addr) = sock.accept()
    
    # client = sock.accept()
    # client_sock = client[0]
    # client_addr = client[1]

        print("Connected client [{}:{}]".format(client_addr[0], client_addr[1]))
        thread = Thread(target=handle_client, args=(client_sock, chat_proto))
        thread.start()

if (__name__ == "__main__"):
    chat_server()