
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StringType

# Step 1: Create SparkSession
spark = SparkSession.builder.appName("ReadJSONExample").getOrCreate()

# Step 2: Define a schema for your JSON data (adjust according to your data)
schema = StructType() \
    .add("name", StringType(), True) \
    .add("age", StringType(), True) \
    .add("location", StringType(), True) \
    .add("_corrupt_record", StringType(), True)

# Step 3: Read the JSON file with the schema
df = spark.read.schema(schema).json(r"C:\Users\Ranjani\Downloads\sample_1000_records.json")

df.show(df.count(), truncate=False)
