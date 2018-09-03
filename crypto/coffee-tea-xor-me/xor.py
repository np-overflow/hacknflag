#!/usr/bin/env python2
import sys

flag = sys.argv[1] 
ciphertext = ""
for i in range(len(flag)):
    encrypted_char = chr(ord(flag[i]) ^ ord(flag[(i+1)%len(flag)]))
    ciphertext += encrypted_char
f = open("ciphertext.txt","w")
f.write(ciphertext)
f.close()