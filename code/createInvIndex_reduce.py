#!/usr/bin/env python

import sys

current_key = None
dictInvIdx = {}

def addToDictionary(word, val):
    # add value to dictionary of inverted index
    if dictInvIdx.get(word) == None:
        invIdx = []
        invIdx.append(val)
        dictInvIdx[word] = invIdx
    else:
        dictInvIdx[word].append(val)

def emitInvIdx(word):
    #print "--------------------------------------"
    invertedIndexes = dictInvIdx[word]
    invIdxStr = str('|'.join(j for j in invertedIndexes))
    print current_key + "::" + invIdxStr
    #print "--------------------------------------"

for line in sys.stdin:
    line = line.strip()
    data = line.split("\t")
    word = data[0]
    val = data[1]

    #print word + "--->" + val

    key = word
    if current_key and (current_key != key) :
        emitInvIdx(current_key)

        del dictInvIdx[current_key]
        current_key = key
        addToDictionary(current_key, val)
    else:
        current_key = key
        addToDictionary(current_key, val)
        #print dictInvIdx

emitInvIdx(current_key)