#!/usr/bin/env python

import sys

for line in sys.stdin:
    line = line.strip()
    data = line.split("::")
    nLineNum = data[0]
    reviewTxt = data[1]

    revWordsLst = reviewTxt.split()
    nPos = 0
    for word in revWordsLst:
        print word + "\t" + nLineNum + "," + str(nPos)
        nPos += 1
    