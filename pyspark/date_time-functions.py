

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, to_date, date_format, hours, date_diff

from pyspark.sql.functions import year

from practice.pyspark.stringfunction import spark

# Create Spark session
# spark = SparkSession.builder \
#     .appName("Date Format Change Example") \
#     .getOrCreate()
# data=[("2024-5-16",),("2024-6-16",),("2024-7-16",),("2024-01-01",)]
# column=["sdate_s"]
#
# s=spark.createDataFrame(data,column)
# s.show()
#
# res=s.withColumn("date", to_date(col("sdate_s")))
# res.show()
#
# df=res.withColumn("edited date",date_format(col("date"),"MM/dd/yyyy"))
# df.show()


s=SparkSession.builder \
    .appName("datefun") \
    .getOrCreate()

a=[("2024-5-16",1),("2024-6-16",2),("2024-7-16",3),("2024-01-01",4)]
a1=["wee","days"]

b=spark.createDataFrame(a,a1)

b1=b.withColumn("newd",to_date(col("wee")))
c=b1.withColumn("eddt",date_format(col("newd"),"dd/MM/yyyy"))
# methods#################################################################################
#date_add()
from pyspark.sql.functions import date_add
# j=c.withColumn("adddate",date_add("newd",5))
# j.show()

# datediff
from pyspark.sql.functions import datediff
h=c.withColumn("diff",date_diff("newd","wee")).show()


# year()
# l=c.withColumn("yer",year("newd")).show()

##################################       Time function     ###############################################

# from pyspark.sql import SparkSession
# from pyspark.sql.functions import col, to_timestamp, current_timestamp, hour, minute, second
#
# sspa = SparkSession.builder \
#     .appName("Time Functions Example") \
#     .getOrCreate()

# # Sample data with date and time
# data = [("2024-05-16 12:30:45",),
#         ("2024-06-16 15:45:30",),
#         ("2024-07-16 08:00:15",),
#         ("2024-01-01 20:15:00",)]
# columns = ["datetime_string"]
#
#
# a=spark.createDataFrame(data,columns)
#
# ss=a.withColumn("timestamp",to_timestamp(col("datetime_string")))
#
# ss.show()


# current timestamp
#
# data = [("Harish", 1), ("Kumar", 2)]
# columns = ["name", "id"]
#
# # DataFrame create panrom
# df = spark.createDataFrame(data, columns)
#
# # current_timestamp add pannanum
# df_with_timestamp = df.withColumn("current_time", current_timestamp())
#
# # Result display pannanumdf_with_timestamp.show(truncate=False)



