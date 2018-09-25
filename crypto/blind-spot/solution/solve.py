#!/usr/bin/env python
import string
chars = string.uppercase+string.lowercase+string.digits+string.punctuation
flag = ""
f = open("some_text.txt","r").read()
for i in f:
    if i in chars:
        flag+=i

print flag
