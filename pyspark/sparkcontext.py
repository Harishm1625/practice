from pyspark.shell import spark

eg=spark.sparkContext

val=[1,2,3,4,5,6,7,8]

rdd=eg.parallelize(val)
f=rdd.sum()
print(f)
l