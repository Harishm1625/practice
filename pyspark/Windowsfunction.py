from pyspark.sql import Window
from pyspark.sql.functions import row_number, window, dense_rank

from practice.pyspark.array import spark

data = [
    ("Alice", "Sales", 1000),
    ("Bob", "Sales", 1500),
    ("Charlie", "Marketing", 2000),
    ("David", "Marketing", 3000),
    ("Eve", "Sales", 1200)
]
columns = ["Employee", "Department", "Salary"]


df=spark.createDataFrame(data,columns)
df.show()

# row number******************************************************************


a=Window.partitionBy("Salary").orderBy("salary")

a1=df.withColumn("Denserank",dense_rank().over(a))


a1.show()



