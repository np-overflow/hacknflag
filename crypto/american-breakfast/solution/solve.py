#!/usr/bin/env python2

#imports
import re
import string

#variable declaration
lookup = {'A':'ttttt', 'B':'ttttr', 'C':'tttrt', 'D':'tttrr', 'E':'ttrtt',
        'F':'ttrtr', 'G':'ttrrt', 'H':'ttrrr', 'I':'trttt', 'J':'trttr',
        'K':'trtrt', 'L':'trtrr', 'M':'trrtt', 'N':'trrtr', 'O':'trrrt',
        'P':'trrrr', 'Q':'rtttt', 'R':'rtttr', 'S':'rttrt', 'T':'rttrr',
        'U':'rtrtt', 'V':'rtrtr', 'W':'rtrrt', 'X':'rtrrr', 'Y':'rrttt',
         'Z':'rrttr', '_':"rrtrt","{":"rrtrr","}":"rrrtt"}
#cipher = "ttrrrtrrtrttrtrrrtrrtrtttrrtrttrtrrtrrrtrtrtrttrttrrtrttrrttttrttrrtrtrttrttrrrttrrttttrttrrtrtttttrttttttttbrtrrrttrrtrtrrtrtrrtrtrrtrtrrtrtrrtrtrrtrrrrtt"
cipher = "ttrrrtrrtrttrtrrrtrrtrtttrrtrttrtrrtrrrtrtrtrttrttrrtrttrrttttrttrrtrtrttrttrrrttrrttttrttrrtrtttttrttttttttrttrrrttrrtrtrrtrtrrtrtrrtrtrrtrtrrtrtrrtrrrrtt"
flag = []
encrypted_chars = re.findall(".....",cipher)

#decoding begins
for i in encrypted_chars:
    flag.append(lookup.keys()[lookup.values().index(i)])

print ''.join(flag)
