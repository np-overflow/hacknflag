#!/usr/bin/env python2

# imports
import string
import itertools
from pwn import * 

guess = string.ascii_lowercase

r = remote("0.0.0.0",8000)
r.recvuntil("flag")
for i in itertools.combinations_with_replacement(guess,5):
    current = ''.join(i)
    r.sendline(current)
    response = r.recv(1024)
    if "HNF{" in response:
        print response
        break 

