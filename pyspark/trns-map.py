from pyspark.python.pyspark.shell import spark

a=spark.sparkContext

lis=[1,2,3,4,5,6,7,8,9]
c=a.parallelize(lis)
f=c.map(lambda x:x % 2 == 0)
s=f.collect()
print(s)


