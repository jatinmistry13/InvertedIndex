#!/usr/bin/python
import sys
import json
default = "-1"
stateCounter={}
attributesCounter={}
categoriesCounter={}
output={}
sep = "|"
fil = open("/Users/vinit/Downloads/yelp/data.json")
for line in fil:
    data = json.loads(line)
    output[data['business_id']] = data
    stateCounter[data['state']] = 1
    if "," in data['categories']:
        categories = data['categories'].split(",")
    else:
        categories = data['categories']
    for category in categories:
        category = category.strip()
        categoriesCounter[category] = 0
    attributes = data['attributes']
    for attribute in attributes:
        #print attributes[attribute]
        if type(attributes[attribute]) is dict:
            #print attributes[attribute]
            for nest in attributes[attribute]:
                #print nest
                attributesCounter[attribute+"*"+nest] = 0
        else:
            attributesCounter[attribute] = 0
final = "business_id"
for attribute in attributesCounter:
    final = final + attribute.encode('utf8') + sep
for category in categoriesCounter:
    final = final + category.encode('utf8') + sep
final = final + "latitude"+sep+"longitude"+sep+"review_count"+sep+"stars"
f3 = open("/Users/vinit/Downloads/states/names.csv","wb")
f3.write(final)
f3.close()
def string_to_int(s):
    ord3 = lambda x : '%.3d' % ord(x)
    return int(''.join(map(ord3, s)))
for state in stateCounter:
    stateFile="/Users/vinit/Downloads/states/"+state.encode('utf8')+".csv"
    stateIdFile="/Users/vinit/Downloads/states/"+state.encode('utf8')+"ID.csv"
    f1 = open(stateFile,"wb")
    f2 = open(stateIdFile,"wb")
    counter = 0
    for id in output:
        data = output[id]
        if data["state"].encode('utf8') != state:
            continue
        lineValue=str(counter)+sep
        idValue = str(id).encode('utf8')+sep+str(counter)
        counter = counter + 1
        attributes = data["attributes"]
        for attribute in attributesCounter:
            if "*" in attribute:
                attribute0 = str(attribute.split("*")[0]).encode('utf8')
                attribute1 = str(attribute.split("*")[1]).encode('utf8')
                nestAttr = attributes.get(attribute0,default)
                if type(nestAttr) is dict:
                    lineValue = lineValue + str(string_to_int(str(nestAttr.get(attribute1,default)))).encode('utf8') + sep
                else:
                    lineValue = lineValue +"45049"+sep
            else:
                lineValue = lineValue + str(string_to_int(str(attributes.get(attribute,default)))).encode('utf8') + sep
        categories = data["categories"]
        for category in categories:
            category = category.strip()
            categoriesCounter[category] = 1
        for categoryValue in categoriesCounter:
            lineValue = lineValue + str(categoriesCounter[categoryValue]).encode('utf8')+sep
        for category in categories:
            category = category.strip()
            categoriesCounter[category] = 0
        lineValue = lineValue + str(data["latitude"]).encode('utf8') + sep + str(data["longitude"]).encode('utf8') + sep + str(data["review_count"]).encode('utf8') + sep + str(data["stars"]).encode('utf8')
        f1.write(lineValue.encode('utf8')+"\n")
        f2.write(idValue.encode('utf8')+"\n")
    f1.close()
