#!/usr/bin/python
import pygmaps
import sys
import os
for file in os.listdir("./"):
    if file.endswith(".csv"):
        f = open(file)
        i = 0
        for line in f:
            latitude =  line.split("|")[863]
            longitude = line.split("|")[864]
            rating = float(line.split("|")[866])
            cluster = line.split("|")[867]
            print rating
            if rating <= 1:
                color="#0000FF"
            elif rating <= 2:
                color="#00FFFF"
            elif rating <= 3:
                color="#008000"
            elif rating <= 4:
                color="#FFFF00"
            else:
                color="#FFA500"
            if i < 1:
                mymap = pygmaps.maps(float(latitude), float(longitude), 10)
            i = i + 1
            mymap.addradpoint(float(latitude), float(longitude), 20, color)
        #mymap = pygmaps.maps(sumLat/i, sumLon/i, 5)
        state = file.split(".")[0]
        mymap.draw('./' + state + '.html')
#mymap = pygmaps.maps(39, -99, 5)
#for line in f:
#    rating = line.split(",")[0]
#    latitude = line.split(",")[1]
#    longitude = line.split(",")[2]
#    rating = float(rating)
#    if rating <= 1:
#        color="#0000FF"
#    elif rating <= 2:
#        color="#00FFFF"
#    elif rating <= 3:
#        color="#008000"
#    elif rating <= 4:
#        color="#FFFF00"
#    else:
#        color="#FFA500"
#    mymap.addradpoint(float(latitude), float(longitude), 50, color)
#mymap.draw('./mymap.html')
