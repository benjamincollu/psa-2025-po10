#!/usr/bin/env python3
from paramiko import SSHClient, AutoAddPolicy

IP_MIKROTIK = "158.193.152.248"
IP_CISCO = "158.193.152.223"
USER = "admin"
PASS = "admin"

ssh = SSHClient()
ssh.set_missing_host_key_policy(AutoAddPolicy())
ssh.connect(IP_CISCO, username=USER, password=PASS)
(stdin, stdout, sterr) = ssh.exec_command("show ip int b")
# count = 0
for line in stdout:
    line_helper = line.strip().strip("\r").split(" ")
    while "" in line_helper:
        line_helper.remove("")
    # if (count == 0):
    if(len(line_helper) < 2):
        continue
    out = (line_helper[0], line_helper[1], line_helper[3], line_helper[4])
    print(out)
    # count += 1

print("--------------------------------------------------")
ssh.connect(IP_MIKROTIK, username=USER, password=PASS)
(stdin, stdout, sterr) = ssh.exec_command("/interface/bridge add name=loCOLLU")
(stdin, stdout, sterr) = ssh.exec_command("/interface/print terse")
# count = 0
for line in stdout:
    print(line)