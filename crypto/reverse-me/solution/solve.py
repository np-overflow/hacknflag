#!/usr/bin/env python2
cipher = open("ciphertext.txt","r").read()
flag = ""
for i in range(len(cipher)):
    decrypted_char = (int(ord(cipher[i])+10) ^ 6)
    flag += chr(decrypted_char)
print flag