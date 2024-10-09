from pyspark.sql.connect.session import SparkSession



one=SparkSession.builder \
    .appName("eg") \
    .getOrCreate()

h1=[('varun',12),('raj',13)]
df=one.createDataFrame(data=h1,schema=['name','age'])

df.show()



