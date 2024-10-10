from pyspark.shell import spark

a=spark.sparkContext

r=[('a',1),('b',2),('c',3),('d',4),('e',5)]


d=a.parallelize(r)

c=d.groupByKey().mapValues(list).collect()
print(c)









