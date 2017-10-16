from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local").setAppName("PopularMovies")
sc = SparkContext(conf = conf)

def loadMovieNames(): 
    movieNames = {}
    with open("../ml-100k/u.ITEM") as f: 
        for line in f: 
            fields = line.split("|")
            movieNames[int(fields[0])] = fields[1]
    return movieNames

nameDict = sc.broadcast(loadMovieNames())

lines = sc.textFile("/Users/mmt7034/code/taming-bigdata-with-apachespark-python/ml-100k/u.data")
movies = lines.map(lambda x : (int(x.split()[1]), 1))
movieCounts = movies.reduceByKey(lambda x, y: x + y)

results = movieCounts.map(lambda (x, y) : (y, x)).sortByKey().map(lambda (x, y) : (y, x)).map(lambda (movie, count): (nameDict.value[movie], count)).collect()

for result in results : 
    print result



