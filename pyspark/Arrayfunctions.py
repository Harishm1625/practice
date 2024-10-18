
from pyspark.sql.functions import array, array_contains, posexplode

from practice.pyspark.stringfunction import spark

data = [(1, 'apple', 'banana', 'cherry'),
        (2, 'mango', 'orange', 'grape')]

df=spark.createDataFrame(data,["id","fruit1","fruit2","fruit3"])


# array function  idhu just namaku venum nu soladra columns elam onna sethu oru array kulla display pannum
# array()
l=df.withColumn("fruit array", array("fruit1","fruit2","fruit3"))
l.show()

# array contains
# Inga namma array_contains() function use panrom, ithu oru array-kulla irukkura specific element irukka nu check panum. Ippo example-la, namma "fruit_array" column-la apple irukka-nu check panrom.

# from pyspark.sql.functions import array_contains
# u=l.withColumn("check",array_contains(l["fruit array"],'apple'))

# u.show()

# ARRAY_LENGTH: The size() function

# Inga size() function use panrom to find the length of an array, adhaavadhu, andha array-la ethana elements irukku-nu kandupidikkanum.

# from pyspark.sql.functions import size
#
# h=l.withColumn("leng", size(l['fruit array']))
# h.show()


# ARRAY_POSITION:
# PySpark-la direct array_position() function illa, aana namma posexplode() function use panni array-la irukkura ellaa element-oda index (position) and value kedaikkum.
# from pyspark.sql.functions import posexplode
# k=l.select('id',posexplode(l["fruit array"]))
# k.show()



# array_remove()
# remove the particular values in the array

from pyspark.sql.functions import *
f=l.withColumn("result",array_remove("fruit array","apple")).show(truncate=False)







