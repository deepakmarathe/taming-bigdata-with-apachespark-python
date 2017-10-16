from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local").setAppName("MaxTemperatures")
sc = SparkContext(conf = conf)

def parseLine(line):
    fields = line.split(',')
    stationId = fields[0]
    recordType = fields[2]
    temperature = float(fields[3]) * 0.1 * (9.0 / 5.0) + 32.0
    return (stationId, recordType, temperature)

lines = sc.textFile("file:///Users/mmt7034/code/taming-bigdata-with-apachespark-python/temperature-dataset/1800.csv")
parsedLines = lines.map(parseLine)

maxTemps = parsedLines.filter(lambda x : "TMAX" in x[1])
stationTemps = maxTemps.map(lambda x : (x[0], x[2]))
maxTemps = stationTemps.reduceByKey(lambda x, y : max(x, y))
results = maxTemps.collect()


for result in results :
    print result[0] , result[1]


