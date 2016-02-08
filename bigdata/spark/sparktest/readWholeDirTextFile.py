"""SimpleApp.py"""
import sys
from pyspark import SparkContext, SparkConf

conf = SparkConf()
conf.setAppName("wholeTextFile test").setMaster("spark://192.168.1.14:7077")
conf.set("spark.cores.max",1)

sc = SparkContext(conf=conf)
textfile = sc.wholeTextFiles("dirtest")

print textfile.count()

def process(x):
	print x
	return 1

res = textfile.map(process).reduce(lambda a, b: a+b)

print res
