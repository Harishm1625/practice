from distutils.text_file import TextFile

from pyspark.shell import spark
from pyspark.sql import SparkSession

# s=SparkSession.builder \
#     .appName("jk") \
#     .getOrCreate()

v=spark.sparkContext


# l=[1,2,3,4,5,6,7,8]
# # rdd transformation inga tha nadakum
# rdd=v.parallelize(l)
#
#
# #rdd action inga nadakum
# rd=rdd.count()
#
# print(rd)

#for reading text file in rdd
#
# ex=v.textFile("contacts.csv")
# bv=ex.count()
# print(bv)



k=[12,13,14,15]

h=v.parallelize(k)
g=h.map(lambda x:x**3)
s=g.collect()
print(s)

j

