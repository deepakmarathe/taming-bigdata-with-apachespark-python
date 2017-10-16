from pyspark import SparkConf, SparkContext
import re


def normalizeWords(text):
    return re.compile(r'\W+', re.UNICODE).split(text.lower())


conf = SparkConf().setAppName("Word-Count better").setMaster("local")
sc = SparkContext(conf=conf)

input = sc.textFile("file:///Users/mmt7034/code/taming-bigdata-with-apachespark-python/word-occurances/Book.txt")
words = input.flatMap(normalizeWords)

wordCounts = words.countByValue()

for word, count in sorted(wordCounts.iteritems(), key=lambda (x, y): (y, x)):
    cleanedWord = word.encode('ascii', 'ignore')
    if (cleanedWord):
        print word, count
