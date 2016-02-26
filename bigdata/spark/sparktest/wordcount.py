from pyspark import SparkContext, SparkConf

conf = SparkConf()
conf.setAppName("deep test").setMaster("spark://192.168.1.14:7077")#.setExecutorEnv("CLASSPATH", path)
conf.set("spark.scheduler.mode", "FAIR")
conf.set("spark.cores.max",44)
conf.set("spark.executor.memory",'5g')

sc = SparkContext(conf=conf)

text_file = sc.textFile("hdfs://titanx4:8020/test/sample.txt")
counts = text_file.flatMap(lambda line: line.split(" ")) \
             .map(lambda word: (word, 1)) \
             .reduceByKey(lambda a, b: a + b)


print counts

counts.saveAsTextFile("hdfs://titanx4:8020/test/result3.txt")

