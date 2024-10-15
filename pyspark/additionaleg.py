from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import IntegerType, StructField

from practice.pyspark.stringfunction import spark

ss=SparkSession.builder \
    .appName("eg") \
    .getOrCreate()

# data=[(1,"Sam"),(2,"Ram")]
#
# df=spark.createDataFrame(data=data , schema=['ID','Name'])


# # with column la when , otherwise use panirukom
#
# #res=df.withColumn("Salary",when(df['Name']=='Sam',20000).otherwise(5000))


# # data type change panirukom cast use pani
# res=df.withColumn(colName='ID',col=col('ID').cast(IntegerType()))
#
# res.printSchema()
#






data=[("1","Hari"),("2","Rex"),("3","sam")]

schema=StructType([
    StructField("id",StringType()),
    StructField("name",StringType())
])
df=spark.createDataFrame(data,schema)

df.show()

