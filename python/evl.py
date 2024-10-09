# # Find the index of the search element in the given list => input = [1, 2, 3, 4, 5], search_element  = 4, output = index of 4 is 3.
#
#
# # write a funciton which will take 2 inputs (1. list 2. search_element) and it should return the output
# s = [1, 2, 3, 4, 5]
#
# def exe():
#      print("index of 4 is",s.index(4))
#
# v=exe()
# print(v)
#

from pyspark import SparkContext

sc = SparkContext("local", "PySpark Basic Example")
data = [1, 2, 3, 4, 5]
rdd = sc.parallelize(data)
print(rdd.collect())  # Collects the data from RDD and returns a list
