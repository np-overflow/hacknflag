#!/usr/bin/env python2

password = "wbown"

guess = False

while not guess:
    print "Enter password for flag"
    user = raw_input()
    if user == password:
        guess = True
print "Here's the flag: HNF{just_pur3_brut3_str3ngth!!}"

