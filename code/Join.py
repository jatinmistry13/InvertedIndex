#!/usr/bin/python
import sys
default = []
clust = {}
for line in sys.stdin:
	features = line.split("|")
	summation = []
	clusNumber = features[867]
	temp = clust.get(int(clusNumber.strip()), default)
	temp.append(features)
	clust[int(clusNumber.strip())] = temp
	temp = []
	default = []
	temp = []
i = 0
for key in clust:
	f = open("stats/" + str(key) + ".csv","wb")
	for item in clust[key]:
		fValue = "" + str(key)
		for it in item:
			fValue = fValue + "|" + it
		f.write(fValue)
	f.close()