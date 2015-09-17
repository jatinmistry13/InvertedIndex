#!/usr/bin/env python

# just count the total occurrence of a word in a specific doc 

import sys


for line in sys.stdin:
    line = line.strip()
    data = line.split("\t")
    key = data[0]
    val = data[1]
    print key + "\t" + val