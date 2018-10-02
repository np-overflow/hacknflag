#!/usr/bin/env python2

# imports
import time

# var setting
flag = "HNF{Ez_t1m1ng_4tt4ck!}"

def check(s):
    if s == flag:
        print "Correct!"
        return
    last_index = len(s) -1
    if s[last_index] == flag[last_index]:
        time.sleep(5)
        return
    else:
        return
a = raw_input("Enter Your Flag: ")
check(a)