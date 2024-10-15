from numpy.f2py.symbolic import integer_types
from pyspark.sql.types import *
from pyspark.sql import SparkSession
from pyspark.sql.types import ArrayType, StringType

spark = SparkSession.builder \
    .appName("name") \
    .getOrCreate()
sc = spark.sparkContext

# ARRAY:

data=[('Sam',['Web']),('Ram',["DE","DS"]),('mythili',["De","maths"])]
schema=StructType([
StructField("name",StringType()),
StructField("skill",StringType())
])
df=spark.createDataFrame(data, schema)
df.show()



# Nested Array:
#
# data = [('Sam', ['Web'], (1, 73026896)), ('Ram', ["DE", "DS"], (2, 98737609)),
#         ('mythili', ["De", "maths"], (3, 2979787))]
# schema = StructType([
# StructField('name',StringType()),
# StructField('skills',StringType()),
# StructField('details',StructType([
#     StructField('id',IntegerType()),
#     StructField("ph",IntegerType())
# ]))
# ])
# df = spark.createDataFrame(data, schema)
# df.show()




