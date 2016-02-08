"""SimpleApp.py"""
import sys
from pyspark import SparkContext, SparkConf

conf = SparkConf()
conf.setAppName("Bad Simple App").setMaster("spark://192.168.1.14:7077")
conf.set("spark.scheduler.mode", "FAIR")
#conf.set("spark.cores.max",4)

sc = SparkContext(conf=conf)
textfile = sc.textFile("hdfs://titanx4:8020/test/b.txt")
res = textfile.map(lambda line: len(line.split())).reduce(lambda a, b: a+b)

print res
