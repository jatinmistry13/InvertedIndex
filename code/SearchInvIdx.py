#!/usr/bin/env python

import sys
import porter2
import time

args = sys.argv

invertedIndex = {}
auxilaryMap = {}

def performStemming(filteredReviewTxt):
    stemmedLst = []
    for word in filteredReviewTxt:
        #print word
        if not word:
            continue
        else:
            stemmedword = porter2.stem(word)
            stemmedLst.append(stemmedword)
    stemmedOutput = str(' '.join(j for j in stemmedLst))
    return stemmedOutput

def addToInvertedIdx(key, posIdx):
    if invertedIndex.get(key) == None:
        valueLst = []
        valueLst.append(posIdx)
        invertedIndex[key] = valueLst
    else:
        invertedIndex[key].append(posIdx)

def readInvertedIndexFile():
    invIdxFile = open("InvertedIndex2.dat", 'r')
    for line in invIdxFile:
        line = line.strip()
        data=line.split("\t")
        keyword = data[0]
        posIdxVal = data[1]
        posIdxLst = posIdxVal.split("|")
        #if keyword == "butcher":
        #    print posIdxLst
        for posIdx in posIdxLst:
            info = posIdx.split(",")
            #if keyword == "butcher":
            #    print "-------------------------"
            #    print keyword
            #    print info
            #    print "-------------------------"
            addToInvertedIdx(keyword, info[0])

def readInvertedIndexFile2():
    invIdxFile = open("InvertedIndex.dat", 'r')
    for line in invIdxFile:
        line = line.strip()
        data=line.split("::")
        keyword = data[0]
        posIdxVal = data[1]
        posIdxLst = posIdxVal.split("|")
        #if keyword == "butcher":
        #    print posIdxLst
        for posIdx in posIdxLst:
            info = posIdx.split(",")
            #if keyword == "butcher":
            #    print "-------------------------"
            #    print keyword
            #    print info
            #    print "-------------------------"
            addToInvertedIdx(keyword, info[0])


def readAuxilaryData():
    auxDataFile = open("preprocess_aux.dat", "r")
    for line in auxDataFile:
        line = line.strip()
        data = line.split("::", 1)

        lineNum = data[0]
        auxVal = data[1]

        auxilaryMap[lineNum] = auxVal

def OneWordSearch():
    resultList = []
    query = args[2]

    pass

def FreeTextSearch(wordList):
    print "In Free Text Search"
    print " Words to search = "
    print wordList
    resultList = []
    for txt in wordList:
        #print invertedIndex.get(txt)
        #resultList.extend(invertedIndex.get(txt))
        #txt = performStemming(txt)
        print txt
        if invertedIndex.get(txt) != None:
            lst = invertedIndex.get(txt)
            resultList.extend(lst)
    #resultList = set(resultList)
    return resultList

def PhraseQuery():
    pass

def LocationSpecificQuery():
    pass

#readAuxilaryData()

stLoadInvIdxTime = time.time()
readInvertedIndexFile()
endLoadInvIdxTime = time.time()
print "Inverted Index load time = " + str(endLoadInvIdxTime - stLoadInvIdxTime) + " seconds..."

def main():
    resultList = None
    print args
    if args[1] == "OWQ:":
        resultList = OneWordSearch()
    elif args[1] == "FTQ":
        resultList = FreeTextSearch(args[2:])
        outData = set(resultList)
        print outData
    elif args[1] == "PQ":
        resultList = PhraseQuery()
    elif args[1] == "LSQ":
        resultList = LocationSpecificQuery()
    else:
        return
    return resultList

if __name__ == "__main__":
    main()