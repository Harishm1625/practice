# from pyspark.shell import spark
#
# v=("Name","Age")
# val=(("hari",22),("tharun",15))
# df=spark.createDataFrame(data=val,schema=v)
#
#
# df.show()
from struct import Struct
from typing import List
from pyspark.shell import spark

# from pyspark.shell import spark

#
# from pyspark.shell import spark
# from pyspark.sql.types import StructField, StringType, IntegerType
#
# from pyspark.python.pyspark.shell import spark
#
#
# v= [(123,235),(125,528)]
# n=('no','sno')
# df = spark.createDataFrame(data=v,schema=n)
#
# df.show()

# #using Dictionary
# m=({'Name':'Hari','Empid':22,'Salary':55555},
#    {'Name':'arun','Empid':20,'Salary':50555},
#    {"Name":"Harish","Empid":25,"Salary":55585})
# dct=spark.createDataFrame(data=m)
#
# dct.show()
#
#
# from pyspark.sql.types import StructType, StructField, StringType, IntegerType
# H=[("hari",22),("tharun",15),("rex",33)]
#
# s=StructType([
#    StructField('Name',StringType()),
#    StructField('Age',IntegerType())
#
# ])
#
# v=spark.createDataFrame(data=H,schema=s)
#
# v.show()
#  Reading a single file:
# df=spark.read.csv(path='data.csv',header=True)
# df.show()


# df=spark.read.format("csv").option('header',True).load('data.csv')
# df.show()

# for reading multiple files at the same time
df = spark.read.csv(path=['data.csv', 'contacts.csv'], header=True)
df.show()

# df=spark.read.csv(path=(),header=True)
# df.show()
































