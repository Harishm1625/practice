from practice.pyspark.stringfunction import spark

a=spark.sparkContext

j=[1,2,3,4,5,6,7,8,9]

m=a.parallelize(j)
c=m.filter(lambda x:x % 2 == 0).collect()
print(c)

