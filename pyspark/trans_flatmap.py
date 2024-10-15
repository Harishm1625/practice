from pyspark.python.pyspark.shell import spark

a=spark.sparkContext

snt=["welcomeatoaDiggibyte"]

s=a.parallelize(snt)

k=s.flatMap(lambda line:line.split("a")).collect()
print(k)



