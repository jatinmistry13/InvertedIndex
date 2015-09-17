#!/usr/bin/env python

# just count the total occurrence of a word in a specific doc 

import sys

current_key = None
lstVal = []

for line in sys.stdin:
    line = line.strip()
    data = line.split("\t")
    key1 = data[0]
    val1 = data[1]

    keysplit = key1.split(",")
    wordkey = keysplit[0]
    linekey = keysplit[1]

    if current_key and (current_key != wordkey):
        outVal = str('|'.join(j for j in lstVal))
        print current_key + "\t" + outVal

        lstVal = []
        current_key = wordkey
        val2 = linekey + "," + val1
        lstVal.append(val2)

    else:
        current_key = wordkey
        val2 = linekey + "," + val1
        lstVal.append(val2)
 
outVal = str('|'.join(j for j in lstVal))
print current_key + "\t" + outVal
lstVal = []