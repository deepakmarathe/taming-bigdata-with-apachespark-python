from pyspark import SparkContext, SparkConf

def parseLine(line):
    fields = line.split(',')
    return (int(fields[0]), float(fields[2]))

conf = SparkConf().setMaster("local").setAppName("Customer Spend Ssorted")
sc = SparkContext(conf = conf)

records = sc.textFile("file:///Users/mmt7034/code/taming-bigdata-with-apachespark-python/assignment-customer-orders/customer-orders.csv")
parsedLines = records.map(parseLine)
customerSpend = parsedLines.reduceByKey(lambda x, y: x + y)
results = customerSpend.map(lambda (x, y): (y, x)).sortByKey().map(lambda (x, y) : (y, x)).collect()

for result in results:
    print result








