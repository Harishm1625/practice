from pyspark.shell import spark

# data frame create panaradhu

# val=(('harish',4500),('raj',5500))
# s=('Name','Salary')
# vd=spark.createDataFrame(data=val,schema=s)
#
# vd.show()


#another method using dictionary

# s=[{'Name':'harish','Salary':4500}]
#
# d=spark.createDataFrame(data=s)
#
# d.show()


#
lg=spark.read.csv(path='data.csv',header=True)

lg.show()


