from pyspark import SparkContext as sc 
rdd = sc.textFile("/word")
rdd.take(5)