from pyspark.python.pyspark.shell import spark
from pyspark.sql.functions import *

# data=[(1,"Hari"),(2,"guru"),(3,"vik"),(4,"Sam")]
#
#
# s=["id","name"]
# a1=spark.createDataFrame(data, s)


# a1.agg(max("id")).show()

# a1.agg(count("id")).show()


# Example data with department information
data = [("Harish", "HR", 23), ("Mohan", "HR", 45),
        ("Lakshmi", "IT", 29), ("Kiran", "IT", 37)]
columns = ["Name", "Department", "Age"]

df = spark.createDataFrame(data, columns)

# Group by Department and apply aggregate functions
k=df.groupBy("Department").agg(sum("Age").alias("Total_Age"), avg("Age").alias("Average_Age")).show()
