from practice.pyspark.stringfunction import spark
from pyspark.sql.functions import expr
data = [(1, [10, 20, 30]), (2, [40, 50, 60]), (3, [70, 80, 90])]

s=spark.createDataFrame(data,["id","nums"])

t=s.withColumn("trnsnums",expr("transform(nums,x -> x+1)"))
t.show()