#!/usr/bin/env python2

# imports
import time
import sys

# var setting
flag = "HNF{Ez_t1m1ng_4tt4ck!}"

def check(s):
    if s == flag:
        print "Correct!"
        sys.stdout.flush()
        return
    last_index = len(s) -1
    if s[last_index] == flag[last_index]:
        time.sleep(5)
        print "no"
        sys.stdout.flush()
        return
    else:
        return
print "Enter Your Flag: "
sys.stdout.flush()
a = raw_input()
check(a)