#!/usr/bin/env python

import sys
import re
import porter2

REVIEWTEXT_TAG = '''"text": '''
USERID_TAG = '''"user_id": '''
REVIEWID_TAG = '''"review_id": '''
REVIEWTEXT_END_TAG = ''', "type":'''
BUSINESS_TAG = '''"business_id": "'''
USERID_IDX = 8
REVIEWID_IDX = 10
RATING_IDX = 12


stopwordsList = []
def getStopWordsList():
    stopwordsFile = open("english.txt", "r")
    for line in stopwordsFile:
        line = line.strip()
        stopwordsList.append(line)


def removeStopWords(reviewText):
    returnLst = []
    reviewTxtLst = reviewText.split()
    for word in reviewTxtLst:
        word = word.strip()
        if not word:
            continue
        if word.endswith("'s"):
            word = word.replace("'s","")
        if word not in stopwordsList:
            returnLst.append(word)
    return returnLst


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


getStopWordsList()
#print stopwordsList
nCnt = 0
for line in sys.stdin:

    line = line.strip()

    # split the line
    data = line.split()

    # get the userid
    #userid = data[USERID_IDX]
    #userid = userid[1:][:-2]

    # get the reviewid
    #reviewid = data[10]
    #reviewid = reviewid[1:][:-2]

    # get the ratings
    #ratingVal = data[12]
    #ratingVal = ratingVal[:-1]

    #busStrtPos = line.index(BUSINESS_TAG) + len(BUSINESS_TAG)
    #busid = line[busStrtPos:-2]

    nCnt += 1
    # get review text
    #print line
    revTxtStartPos = line.index(REVIEWTEXT_TAG) + len(REVIEWTEXT_TAG)
    revTxtEndPos = line.index(REVIEWTEXT_END_TAG)
    reviewText = line[revTxtStartPos+1:revTxtEndPos-1]

    # convert review text to lowercase
    reviewText = reviewText.lower()

    #reviewText = re.sub("'", "", reviewText)
    reviewText = re.sub(r"'", "", reviewText)
    reviewText = re.sub(r"\s+", " ", reviewText)
    reviewText = re.sub('[^A-Za-z0-9]+', ' ', reviewText)

    #print nCnt
    #print reviewText

    #reviewText = reviewText.replace("'","_")
    #print reviewText

    # filter stop words
    filteredReviewTxt = removeStopWords(reviewText)
    #print filteredReviewTxt

    # perform stemming on the remaining word
    stemmedReview = performStemming(filteredReviewTxt)

    #print userid + "::" + reviewid + "::" + ratingVal + "::" + stemmedReview
    print str(nCnt) + "::" + stemmedReview

