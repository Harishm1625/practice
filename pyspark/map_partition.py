from gc import collect
from os.path import split
from turtledemo.sorting_animate import partition

from pyspark.python.pyspark.shell import spark

a=spark.sparkContext

# l=[1,2,3,4,5,6,7,8,9]
#
# s=a.parallelize(l)
#
# c=s.mapPartitions(lambda partition:(i * 2 for i in partition)).collect()
#
# print(c)
#


#partition with index



# l=[1,2,3,4,5,6,7,8,9]
#
# v=a.parallelize(l,2)
#
# z=v.mapPartitionsWithIndex(lambda idx, partition:(idx,sum(partition))).collect()
#
# print(z)


k=[1,2,3,4,5,6,7,8,9]
h=a.parallelize(k)
def sap(x):
    return (x*2 for x in k)

b=h.mapPartitions(sap).collect()

print(b)