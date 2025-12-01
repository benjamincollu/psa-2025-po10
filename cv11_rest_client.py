#!/usr/bin/env python3
import requests

IP_MIKROTIK = "158.193.152.248"
IP_CISCO = "158.193.152.223"
USER = "admin"
PASS = "admin"
BASE_URL = "http://{}:80/rest".format(IP_MIKROTIK)

body = {"name":"lo22"}
resp = requests.put(BASE_URL+"/int/bridge", auth=(USER, PASS), json=body)
print(resp.status_code)

resp = requests.get(BASE_URL+"/int", auth=(USER, PASS))
print(resp.status_code)
if resp.status_code == 200:
    body = resp.json()
    for interface in body:
        print(interface["name"])