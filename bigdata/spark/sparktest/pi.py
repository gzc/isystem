from pyspark import SparkContext, SparkConf
from random import random

conf = SparkConf()
conf.setAppName("deep test").setMaster("spark://192.168.1.14:7077")#.setExecutorEnv("CLASSPATH", path)
conf.set("spark.scheduler.mode", "FAIR")
conf.set("spark.cores.max",44)
conf.set("spark.executor.memory",'5g')
#conf.set("spark.scheduler.allocation.file", "./scheduler.xml")

sc = SparkContext(conf=conf)

NUM_SAMPLES=10000


def sample(p):
    x, y = random(), random()
    return 1 if x*x + y*y < 1 else 0

count = sc.parallelize(xrange(0, NUM_SAMPLES)).map(sample) \
             .reduce(lambda a, b: a + b)
print "Pi is roughly %f" % (4.0 * count / NUM_SAMPLES)

