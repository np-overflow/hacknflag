#!/usr/bin/env python2

# imports
import string

flag = "HNF{I_LOVE_ME_SOME_BACONNNNNNN}"
lookup = {'A':'ttttt', 'B':'ttttr', 'C':'tttrt', 'D':'tttrr', 'E':'ttrtt',
        'F':'ttrtr', 'G':'ttrrt', 'H':'ttrrr', 'I':'trttt', 'J':'trttr',
        'K':'trtrt', 'L':'trtrr', 'M':'trrtt', 'N':'trrtr', 'O':'trrrt',
        'P':'trrrr', 'Q':'rtttt', 'R':'rtttr', 'S':'rttrt', 'T':'rttrr',
        'U':'rtrtt', 'V':'rtrtr', 'W':'rtrrt', 'X':'rtrrr', 'Y':'rrttt',
         'Z':'rrttr', '_':"rrtrt","{":"rrtrr","}":"rrrtt"}
encrypted = []
for i in flag:
    encrypted_char = lookup[i]
    encrypted.append(encrypted_char)
print ''.join(encrypted)
        
