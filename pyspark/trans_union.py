from pyspark.python.pyspark.shell import spark

a=spark.sparkContext

s=[1,2,3,4,5]
k=[1,2,3,4,5]

j=a.parallelize(s)
l=a.parallelize(k)

c=j.union(l).collect()

print(c)

