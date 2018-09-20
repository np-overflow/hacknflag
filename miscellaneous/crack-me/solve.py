#!/usr/bin/env python2

# imports
import string
import itertools
from subprocess import Popen,PIPE,STDOUT
import sys

guess = string.ascii_lowercase



for i in itertools.combinations_with_replacement(guess,5):
    current = ''.join(i)
    p = Popen(["python","crack-me.py"],stdin=PIPE,stdout=PIPE,stderr=STDOUT,bufsize=1)
    response =  p.communicate(current)[0]
    print current
    print response
    if "HNF{" in response:
        print "The password was {}".format(current)
        print response
        break 

