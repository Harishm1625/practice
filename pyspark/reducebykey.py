from pyspark.python.pyspark.shell import spark

a=spark.sparkContext

rdd = a.parallelize([('A', 1), ('B', 2), ('A', 3), ('B', 4)])
result = rdd.reduceByKey(lambda x, y: x + y).collect()
print(result)
