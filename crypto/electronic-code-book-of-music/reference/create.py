#!/usr/bin/env python2

# imports
from Crypto.Cipher import AES
from hashlib import md5
from base64 import b64encode

# finding MD5 hash of composers to form the key
key = md5("beethovenchopin").hexdigest()
print len(key)
# Initialise the cipher
cipher = AES.new(key,AES.MODE_ECB)

# open the plaintext file
with open("private.png",'r') as text:
    plaintext = text.read()
    text.close()

# make the plaintext into multiple of 16 for AES encryption
plaintext = plaintext[::-1].zfill(27952)[::-1]

# encode the ciphertext
ciphertext = b64encode(cipher.encrypt(plaintext))

# write ciphertext to file
'''with open("private.txt","w") as private:
    private.write(ciphertext)
    private.close()'''