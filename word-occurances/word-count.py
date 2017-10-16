from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local").setAppName("WordCount")
sc = SparkContext(conf =  conf)

input = sc.textFile("file:///Users/mmt7034/code/taming-bigdata-with-apachespark-python/word-occurances/Book.txt")
words = input.flatMap(lambda x : x.split())
wordCounts = words.countByValue()

for word, count in sorted(wordCounts.iteritems(), key = lambda (k, v) : (v, k)):
    cleanWord = word.encode('ascii', 'ignore')
    if (cleanWord): 
        print cleanWord, count


