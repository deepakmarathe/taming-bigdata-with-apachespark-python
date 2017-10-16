from pyspark import SparkConf, SparkContext

def parseLine(line):
    fields = line.split(",")
    customerId = int(fields[0])
    spend = float(fields[2])
    return (customerId, spend)

conf = SparkConf().setAppName("Customer-Spend").setMaster("local")
sc = SparkContext(conf = conf)

lines = sc.textFile("file:///Users/mmt7034/code/taming-bigdata-with-apachespark-python/assignment-customer-orders/customer-orders.csv")
customerSpend = lines.map(parseLine)
results = customerSpend.reduceByKey(lambda x, y: x + y).collect()

for result in results: 
    print result[0], " : ", result[1]



