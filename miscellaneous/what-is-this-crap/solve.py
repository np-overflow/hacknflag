#!/usr/bin/env python2
f1 = open("text1.txt","r").read()
f2 = open("text2.txt","r").read()
flag1 = ""
flag2 = ""
for i in range(len(f1)):
    if f1[i] != f2[i]:
        flag1 += f1[i]
        flag2 += f2[i]
if flag1[:3] == "HNF":
    print flag1
else:
    print flag2
        
