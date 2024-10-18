# id name  sal
# 1   vinay   1000
# 2   vinay    1000
# 3  vinay      3000
# 4   b            1000
from turtledemo.sorting_animate import partition

from pyspark.sql import Window
from pyspark.sql.functions import *

from practice.pyspark.json_practice import spark

# sql***********

data=[(1,"vinay",1000),(2,"vinay",1000),(3,"vinay",3000),(4,"b",1000)]
col=["id","name","sal"]

df=spark.createDataFrame(data,col)

s=Window.partitionBy("name").orderBy("sal").Desc

res=df.withColumn("rank",rank().over(s)).show()



