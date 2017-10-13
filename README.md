#Course : Taming bigdata with apache spark - Hands on

## Apache spark

* massive data processing
* python programming language
* 15 hands on spark python scripts
* business problems into spark problesm, work on spark problem and analyse.
	- movies data : movie recommendations
	- superheroes data : find degrees of separation

## Spark installation(Mac Os) :
Resource : http://media.sundog-soft.com/spark-python-install.pdf

    brew install apache-spark

    cd /usr/local/Cellar/apache-spark/2.2.0/libexec/conf
    cp log4j.properties.template log4j.properties

    Edit the log4j.properties file and change the log level from INFO to ERROR on log4j.rootCategory.

## Verification of the installation :

    cd ‘some directory’
    pyspark
    rdd = sc.textFile("README.md")
    rdd.count()
    quit()


## Python Installation :
Use anaconda distribution of python. I am working with python 2.7
