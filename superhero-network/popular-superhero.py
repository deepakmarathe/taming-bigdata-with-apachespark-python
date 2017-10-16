from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local").setAppName("MostPopularSuperHero")
sc = SparkContext(conf = conf)

def countCoOccurances(line):
    elements = line.split()
    return (int(elements[0]), len(elements) - 1)

def parseNames(line):
    fields = line.split('\"')
    return (int(fields[0]), fields[1].encode("utf8"))



names = sc.textFile("file:///Users/mmt7034/code/taming-bigdata-with-apachespark-python/superhero-network/Marvel-Names.txt")
namesRdd = names.map(parseNames)

lines = sc.textFile("file:///Users/mmt7034/code/taming-bigdata-with-apachespark-python/superhero-network/Marvel-Graph.txt")
pairings = lines.map(countCoOccurances)
totalFriendsByCharacter = pairings.reduceByKey(lambda x, y: x + y)

mostPopular = totalFriendsByCharacter.map(lambda (x, y) : (y, x)).max()
mostPopularName = namesRdd.lookup(mostPopular[1])[0]

print mostPopularName, mostPopular[0]

