from pyspark import SparkConf, SparkContext
import collections

conf = SparkConf().setMaster("local").setAppName("RatingsHistogram")
sc = SparkContext(conf = conf)


rdd = sc.textFile("/Users/mmt7034/code/taming-bigdata-with-apachespark-python/README.md")
print "number of lines in README.md file : ", rdd.count()



