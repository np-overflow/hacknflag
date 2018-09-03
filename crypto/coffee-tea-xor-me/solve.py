#!/usr/bin/env python2
ciphertext = open("ciphertext.txt","r").read()

flag = "H"
for i in range(len(ciphertext)-1): #-1 as the last char is xor-ed with the 1st char to form H
    decrypted_char = chr(ord(ciphertext[i]) ^ ord(flag[i]))
    flag += decrypted_char
print flag