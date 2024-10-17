from practice.pyspark.array import spark

data1 = [(1, 'Ram'), (2, 'Sam'), (3, 'Babu')]

data2 = [(1, 'M'), (2, 'F'), (4, 'F')]

column1=["id","name"]
column2=["id","gender"]
c=spark.createDataFrame(data1,column1)
d=spark.createDataFrame(data2,column2)


s=c.union(d)
s.show()


# Remove duplicates
s.distinct.show()
