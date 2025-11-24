#!/usr/bin/env python3

import socket
import struct

DNS_SERVER = "8.8.8.8"
DNS_PORT = 53


transaction_id = 0x1234
flags = 0x0100  # standard query
dns_header = struct.pack("!6H", transaction_id, flags, 1, 0, 0, 0)

question = input("Enter domain name to resolve: ")
labels = question.split(".")
labels_bytes = bytes()

for label in labels:
    labels_bytes += struct.pack("B", len(label))
    labels_bytes += label.encode()

labels_bytes += struct.pack("B", 0)  # end of QNAME
question_type = 1 # A record
question_byte = labels_bytes + struct.pack("!2H", question_type, 0x0001)  # QTYPE=A, QCLASS=IN

dns_bytes = dns_header + question_byte
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(dns_bytes, (DNS_SERVER, DNS_PORT))

(received_bytes, address) = sock.recvfrom(1000)
print("Received {} bytes from {}".format(len(received_bytes), address))
print(received_bytes.hex())

# if received_bytes[0:2] == struct.pack("!H", transaction_id):
# int.from_bytes(received_bytes[0:2], "big") == transaction_id
if received_bytes[0:2] == struct.pack("!H", transaction_id):
    ip_addr = socket.inet_ntoa(received_bytes[-4:])  # last 4 bytes (IP address)
    print(ip_addr)

sock.close()