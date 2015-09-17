#!/usr/bin/env python

# just count the total occurrence of a word in a specific doc 

import sys

current_key = None
lstVal = []

for line in sys.stdin:
    line = line.strip()
    data = line.split("\t")
    key = data[0]
    val = data[1]

    if current_key and (current_key != key):
        outVal = str('|'.join(j for j in lstVal))
        print key + "\t" + outVal

        lstVal = []
        current_key = key
        lstVal.append(val)
    else:
        current_key = key
        lstVal.append(val)

outVal = str('|'.join(j for j in lstVal))
print key + "\t" + outVal
lstVal = []