# -*- coding: utf-8 -*-
from pyspark.mllib.clustering import KMeans, KMeansModel
from numpy import array
from math import sqrt
from pyspark import SparkContext, SparkConf

conf = SparkConf()
conf.setAppName("deep test")#.setMaster("spark://192.168.1.14:7077")#.setExecutorEnv("CLASSPATH", path)
#conf.set("spark.scheduler.mode", "FAIR")
#conf.set("spark.cores.max",44)
#conf.set("spark.executor.memory",'5g')

sc = SparkContext(conf=conf)

# Load and parse the data
data = sc.textFile("kmeans_data.txt")
parsedData = data.map(lambda line: array([float(x) for x in line.split(' ')]))

# Build the model (cluster the data)
clusters = KMeans.train(parsedData, 2, maxIterations=10,
        runs=10, initializationMode="random")

# Evaluate clustering by computing Within Set Sum of Squared Errors
def error(point):
    center = clusters.centers[clusters.predict(point)]
    return sqrt(sum([x**2 for x in (point - center)]))

WSSSE = parsedData.map(lambda point: error(point)).reduce(lambda x, y: x + y)
print("Within Set Sum of Squared Error = " + str(WSSSE))

# Save and load model
clusters.save(sc, "myModelPath")
sameModel = KMeansModel.load(sc, "myModelPath")
