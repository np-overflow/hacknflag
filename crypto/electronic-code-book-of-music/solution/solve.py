#!/usr/bin/env python2

# imports
from hashlib import md5
from Crypto.Cipher import AES
from base64 import b64decode

# open ciphertext to decrypt
with open("challenge/private.txt","r") as private:
    ciphertext = private.read()
    private.close()

# base64 decode
ciphertext = b64decode(ciphertext)

# get key
key = md5("beethovenchopin").hexdigest()
print len(key)

# Initialise AES cipher and decrypt
cipher = AES.new(key,AES.MODE_ECB)
plaintext = cipher.decrypt(ciphertext)

# write plaintext into new file
with open("flag","w") as flag:
    flag.write(plaintext)
    flag.close()


    