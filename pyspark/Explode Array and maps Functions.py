from pyspark.sql.connect.functions import explode, explode_outer, posexplode, posexplode_outer

from practice.pyspark.stringfunction import spark

data = [("1", ["a", "b", "c"]), ("2", ["d", "e"])]

s=spark.createDataFrame(data,['id','letters'])

s.show()

# explode()

# explode() function use pannum, array or map column-a separate rows-a convert panna. Oru array la irundha ellaa elements-kum oru row create pannum.
# from pyspark.sql.functions import explode
# x=s.select(s.id,explode(s.letters).alias('new let')).show()


# explode_outer()
# Definition:
# explode_outer() function explode() maathiri work pannum, aana null values-a handle pannum. Array or map column null irundhaalum, athai skip pannaama oru row return pannum.
#
from pyspark.sql.functions import explode_outer
data = [("1", ["a", "b", "c"]), ("2", None)]

a=spark.createDataFrame(data,['id','values'])
a.show()

d=a.select(a.id,explode_outer(a.values).alias('expout')).show()

#  posexplode()
# Definition:
# posexplode() function explode() maathiri, aana ithu values kooda position (index) kooda kudukkum. Array or map la element position-a paathukalam.

#
# from pyspark.sql.functions import posexplode
# w=s.select(s.id,posexplode(s.letters).alias("pos","newlit")).show()


#posexplode_outer()
# Definition:
# posexplode_outer() function posexplode() maathiri, aana ithu null values-a handle pannum. Array or map null irundhaalum oru row create aagum.
from pyspark.sql.functions import posexplode_outer
v=s.select(s.id,posexplode_outer(s.letters).alias("pos","let")).show()








