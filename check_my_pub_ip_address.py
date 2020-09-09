#!/usr/bin/python3

import os

#last update = today

ip = os.popen('dig +short myip.opendns.com @resolver1.opendns.com').readlines(-1)[0].strip()

print(ip)
