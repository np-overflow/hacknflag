#!/usr/bin/env python2
import sys
flag = sys.argv[1]
flag_list = []
encrypted_list = []
for i in flag:
    flag_list.append(ord(i))

for i in range(len(flag_list)):
    encrypted_char = (flag_list[i] ^ 6) -10
    encrypted_list.append(encrypted_char)
encrypted_flag = ""
for i in encrypted_list:
    encrypted_flag += chr(i)
ciphertext = open("ciphertext.txt","w")
ciphertext.write(encrypted_flag)
ciphertext.close()

