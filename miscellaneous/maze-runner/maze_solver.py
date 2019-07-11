
#!/usr/bin/env python
from pwn import *

# if direction is <, then the first item is the icon to the left of said direction, 2nd item is icon infront of said direction
'''
0 1 2
3 4 5
6 7 8
This is the how the map icons indexes are interpreted when converted to a list
'''

'''
E.g when a runner faces like this <,
the 7th index in the map list is to the left of that runner,
the 3th index in the map list is to the front of the runner,
the 1st index in the map list is to the right of the runner
'''
# lefting stores the indicies of the map on what would be the left, front and right of the runner relative to its position
lefting = {
    "<": (7, 3, 1),
    "^": (3, 1, 5),
    ">": (1, 5, 7),
    "v": (5, 7, 3),
}

# This is to store the up, down, left, right indices of the 3x3 grid to the direction of the keyboard
key_map = {
    1: "W",
    3: "A",
    5: "D",
    7: "S",
}


def turn_right(curr_dir):
    if curr_dir == "<":
        return "^"
    if curr_dir == "^":
        return ">"
    if curr_dir == ">":
        return "v"
    if curr_dir == "v":
        return "<"


def turn_left(curr_dir):
    if curr_dir == "<":
        return "v"
    if curr_dir == "v":
        return ">"
    if curr_dir == ">":
        return "^"
    if curr_dir == "^":
        return "<"


def flip_dir(curr_dir):
    if curr_dir == "<":
        return ">"
    if curr_dir == "v":
        return "^"
    if curr_dir == ">":
        return "<"
    if curr_dir == "^":
        return "v"


# curr_m is current map
# curr_d is curr_d

# This is to find what key to press next
def find_next_key(curr_m, curr_d):
    starting_surroundings = list(curr_m)
    map_strip = []
    next_d = ""
    # Take in the map and remove unneeded spaces and newlines
    for ind, ico in enumerate(starting_surroundings):
        if ind in range(0, 17, 2):
            map_strip.append(ico)
    # Find what is to the left, right and front of the runner relative to its direction
    front = map_strip[lefting[curr_d][1]]
    left = map_strip[lefting[curr_d][0]]
    right = map_strip[lefting[curr_d][2]]
    print(left, front, right)
    # Runner logic, priority for it to go left is left is open, followed by front if left is closed
    # If front is also closed, turn right and go instead
    # If all 3 are closed, flip direction and go through the same logic
    if left == " " or left == "!":
        next_d = turn_left(curr_d)
        key = key_map[lefting[next_d][1]]
    elif front == " " or front == "!":
        next_d = curr_d
        key = key_map[lefting[next_d][1]]
    elif right == " " or right == "!":
        next_d = turn_right(curr_d)
        key = key_map[lefting[next_d][1]]
    else:
        next_d = flip_dir(curr_d)
        key = key_map[lefting[next_d][1]]
    return key, next_d


r = remote('ctf.yadunut.com', 8004)
r.recvline()
next_dir = '>'
while True:
    tmp = r.recv()
    print("MAP")
    print(tmp)
    key, next_dir = find_next_key(tmp, next_dir)
    print(key, next_dir)
    r.sendline(key)
