#Course : Taming bigdata with apache spark - Hands on

## Apache spark

* massive data processing
* python programming language
* 15 hands on spark python scripts
* business problems into spark problesm, work on spark problem and analyse.
	- movies data : movie recommendations
	- superheroes data : find degrees of separation

## Java Installation 
    follow the standard steps for installting java from oracle's website. 
    
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


Introduction to spark : 
    
    what is spark : a fast and general engine for large-scale data processing
    divide and conquer - split large data into multiple machines and process them parallely.
   
    Run programs upto 100x faster than Hadoop MapReduce in memory, or 10x faster on disk.
    
    DAG engine (directed acyclic graph) optimizes workflows
    
    Code in Python,Java, or Scala
    
    Built around one main concept : the Resilient Distributed Dataset (RDD)
    
    Transforming RDD's : 
        map
        flatmap
        filter
        distinct
        sample
        union, intersection, subtract, cartesian 
    Actions on RDD's :  
        collect
        count
        countByValue
        take
        top
        reduce   