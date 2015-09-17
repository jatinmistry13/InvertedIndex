import sys
from pyspark import SparkContext, SparkConf

conf = SparkConf().setAppName("vinit").setMaster("local")
sc = SparkContext(conf=conf)

from math import ceil
from numpy import array
from math import sqrt
from pyspark.mllib.clustering import KMeans

def error(point):
    # Evaluate clustering by computing Within Set Sum of Squared Errors
    center = clusters.centers[clusters.predict(point)]
    return sqrt(sum([x**2 for x in (point - center)]))

def prt(x):
	print x

state = "CA.csv"

data = sc.textFile("/Users/vinit/Downloads/states/"+state)
parsedData = data.map(lambda line: array([float(x) for x in line.split('|')]))

K = int(ceil(sqrt(parsedData.count())))

clusters = KMeans.train(parsedData, K, maxIterations=1000,initializationMode="k-means||")

clAs = parsedData.map(lambda line: str(line[0]) + "," +str(clusters.predict(line)))

clAs.saveAsTextFile(state)

WSSSE = parsedData.map(lambda point: error(point)).reduce(lambda x, y: x + y)
print("Within Set Sum of Squared Error = " + str(WSSSE))
