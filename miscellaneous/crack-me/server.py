#!/usr/bin/env python2

password = "wbown"
counter = 0
guess = False

while not guess:
    print "Enter password for flag"

    user = raw_input()
    counter += 1
    if user == password or counter >= 1000:
        print "Here's the flag: HNF{just_pur3_brut3_str3ngth!!}"
        guess = True

