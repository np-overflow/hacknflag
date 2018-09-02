import time
flag = "HNF{Ez_t1m1ng_4tt4ck}"
def check(s):
    for c in range(min(len(s), len(flag))):
        if c < 3 and flag[c] == s[c]:
            time.sleep(1)
        if flag[c] == s[c]:
            time.sleep(0.3)
        else:
            print("no")
            return
    if len(s) != len(flag):
        print("no")
        return
    print("You got it!")
    return

a = input("Enter the flag: ")
check(a)
