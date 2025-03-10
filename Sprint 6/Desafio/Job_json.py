import sys
from awsglue.transforms import * # type: ignore
from awsglue.utils import getResolvedOptions# type: ignore
from pyspark.context import SparkContext
from awsglue.context import GlueContext# type: ignore
from awsglue.job import Job# type: ignore
from pyspark.sql.functions import *
from pyspark.sql.types import *

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME', "S3_INPUT_PATH", "S3_TARGET_PATH"])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

input_path = args["S3_INPUT_PATH"]
target_path = args["S3_TARGET_PATH"]

# leitura dos json
df_json = spark.read.option("multiline", "true").json(input_path)

# Concerta as colunas
df_json = df_json.select(explode(df_json.movies)).selectExpr("col.*")

# Remove linhas duplicatas/nulas
df_json = df_json.dropDuplicates().dropna(how="all")

# Escrevendo s3
df_json.write \
    .mode("overwrite") \
    .format("parquet") \
    .save(target_path)

job.commit()