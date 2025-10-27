#! /usr/bin/env python3

from cv05_chat_protocol import Chat_proto, Ctrl_value
import socket as s

IP = "127.0.0.1"
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


def chat_client():
    nick = input("Enter nickname: ")
    chat_proto = Chat_proto(nick)

    #ip, tcp
    sock = s.socket(s.AF_INET, s.SOCK_STREAM)
    sock.connect((IP, PORT)) # bind ocakava jeden parameter - adresu - socket

    # send login message to server
    msg_bytes = chat_proto.login().encode()
    sock.send(msg_bytes)

    while True:
        print("Menu:")
        print(" 1. Send message")
        print(" 2. Get users list")
        print(" 3. Logout")
        choice = input("Enter choice: ")
        print()

        if choice[0] == "1":
            text_msg = input("Enter message: ")
            msg_bytes = chat_proto.msg(text_msg).encode()
            sock.send(msg_bytes)
        elif choice[0] == "2":
            msg_bytes = chat_proto.users().encode()
            sock.send(msg_bytes)
            users_bytes = sock.recv(1000).decode()
            print("Logged in users: ")
            print(users_bytes)
            input("Press Enter to continue...")
            return
        elif choice[0] == "3":
            msg_bytes = chat_proto.logout().encode()
            sock.send(msg_bytes)
            sock.close()
            return
    
    # client = sock.accept()
    # client_sock = client[0]
    # client_addr = client[1]

if (__name__ == "__main__"):
    chat_client()