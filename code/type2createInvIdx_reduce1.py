#!/usr/bin/env python

# just count the total occurrence of a word in a specific doc 

import sys

current_key = None
sum = 0

for line in sys.stdin:
    line = line.strip()
    data = line.split("\t")
    key = data[0]
    val = int(data[1])

    if current_key and (current_key != key):
        print current_key + "\t" + str(sum)

        sum = 0
        current_key = key
        sum = sum + val

    else:
        current_key = key
        sum = sum + val

print key + "\t" + str(sum)