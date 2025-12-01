#!/usr/bin/env python3
from netmiko import ConnectHandler

IP_MIKROTIK = "158.193.152.248"
IP_CISCO = "158.193.152.223"
USER = "admin"
PASS = "admin"

config = {
    "device_type": "cisco_ios",
    "host": IP_CISCO,
    "username": USER,
    "password": PASS   
}

ssh = ConnectHandler(**config)
add_loop = [
    "conf t",
    "int lo22",
    "ip add 192.0.22.1 255.255.255.255"
]
ssh.send_config_set(add_loop)
output = ssh.send_command("show ip int b")
print(output.split("\n"))
print(output)