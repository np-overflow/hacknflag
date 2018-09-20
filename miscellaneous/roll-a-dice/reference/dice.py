#!/usr/bin/env python2

import random
flag = 96110844387941543913051206312708500349

num = random.randint(1,6)
print "Welcome to my guessing game.\nSimply guess what number my dice will roll and the flag shall be yours."
user = int(raw_input("Enter Your Guess: "))
if user == num:
    print "You got it!!!\n\nThe flag is {}".format(hex(flag)[2:-1].decode('hex'))
else:
    print "try again"
