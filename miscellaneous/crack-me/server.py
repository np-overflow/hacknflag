#!/usr/bin/env python2
import sys

password = "wbown"
counter = 0
guess = False

while not guess:
    print "Enter password for flag"
    sys.stdout.flush()

    user = raw_input()
    counter += 1
    if user == password or counter >= 1000:
        print "Here's the flag: HNF{just_pur3_brut3_str3ngth!!}"
        sys.stdout.flush()
        guess = True

