from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local").setAppName("PopularMovies")
sc = SparkContext(conf = conf)

lines = sc.textFile("/Users/mmt7034/code/taming-bigdata-with-apachespark-python/ml-100k/u.data")
movies = lines.map(lambda x : (int(x.split()[1]), 1))
movieCounts = movies.reduceByKey(lambda x, y: x + y)

results = movieCounts.map(lambda (x, y) : (y, x)).sortByKey().map(lambda (x, y) : (y, x)).collect()

for result in results : 
    print result



