from pyspark import SparkConf, SparkContext
import collections

conf = SparkConf().setMaster("local").setAppName("Simple app")
sc = SparkContext(conf = conf)

dataset = sc.parallelize([1, 2, 3, 4, 5])
squares = dataset.map(lambda x: x * x)
print squares.collect()


