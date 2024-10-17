# joins in rdd
from pyspark.python.pyspark.shell import spark
#
# sc = spark.sparkContext
#
# data1 = [(1, 'Ram'), (2, 'Sam'), (3, 'Babu')]
# data2 = [(1, 'M'), (2, 'F'), (4, 'F')]
#
# rdd1 = sc.parallelize(data1)
# rdd2 = sc.parallelize(data2)
#
# res = rdd1.leftOuterJoin(rdd2)
#
# for x in res.collect():
#     print(x)
from pyspark.sql.connect.functions import broadcast

from practice.pyspark.stringfunction import spark

# joins in dataframe

data1 = [(1, 'Ram'), (2, 'Sam'), (3, 'Babu')]

data2 = [(1, 'M'), (2, 'F'), (4, 'F')]
column1=["id","name"]
column2=["id","gender"]
c=spark.createDataFrame(data1,column1)
d=spark.createDataFrame(data2,column2)

# a=c.join(d,"id","right").show()

s=c.join(d,c.id == d.id,"leftanti")
s.show()
#
#
# from pyspark.sql import SparkSession
# from pyspark.sql.functions import broadcast
#
# # Create a Spark session
# spark = SparkSession.builder.appName("Broadcast Join Example").getOrCreate()
#
# # Data for DataFrames
# data1 = [(1, 'Ram'), (2, 'Sam'), (3, 'Babu')]
# data2 = [(1, 'M'), (2, 'F'), (4, 'F')]
#
# # Define columns
# column1 = ["id", "name"]
# column2 = ["id", "gender"]
#
# # Create DataFrames
# c = spark.createDataFrame(data1, column1)
# d = spark.createDataFrame(data2, column2)
#
# # Perform broadcast join
# result = c.join(broadcast(d), "id")
# result.show()
