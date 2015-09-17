#!/usr/bin/env python

# just count the total occurrence of a word in a specific doc 

import sys

for line in sys.stdin:
    line = line.strip()
    data = line.split("::")
    nLineNum = data[0]
    reviewTxt = data[1]

    revWordsLst = reviewTxt.split()
    for word in revWordsLst:
        print word + "," + nLineNum + "\t" + str(1)
