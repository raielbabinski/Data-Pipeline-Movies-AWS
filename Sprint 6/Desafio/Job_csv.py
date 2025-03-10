import sys
from awsglue.transforms import *# type: ignore
from awsglue.utils import getResolvedOptions# type: ignore
from pyspark.context import SparkContext# type: ignore
from awsglue.context import GlueContext# type: ignore
from awsglue.job import Job # type: ignore
from pyspark.sql.functions import *
from pyspark.sql.types import *


## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME', 
                                    "S3_INPUT_PATH_MOVIES", 
                                    "S3_INPUT_PATH_SERIES",
                                    "S3_TARGET_PATH_MOVIES",
                                    "S3_TARGET_PATH_SERIES"
                                    ]
)

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

input_series = args["S3_INPUT_PATH_SERIES"]
input_movies = args["S3_INPUT_PATH_MOVIES"]
target_series = args["S3_TARGET_PATH_SERIES"]
target_movies = args["S3_TARGET_PATH_MOVIES"]

# ---------------- Processo movies.csv --------------------

# Leitura do csv
df_movies = spark.read.csv(input_movies, header=True, sep="|")

# Renomeção e tipagem das colunas
df_movies = df_movies.withColumnRenamed("tituloPincipal", "tituloPrincipal")
df_movies = df_movies.withColumn("anoLancamento", col("anoLancamento").cast("int")) \
                     .withColumn("tempoMinutos", col("tempoMinutos").cast("int")) \
                     .withColumn("notaMedia", col("notaMedia").cast("double")) \
                     .withColumn("numeroVotos", col("numeroVotos").cast("int")) \
                     .withColumn("anoNascimento", col("anoNascimento").cast("int")) \
                     .withColumn("anoFalecimento", col("anoFalecimento").cast("int"))

# Remoção de linhas duplicatas e nulas
df_movies = df_movies.dropDuplicates()
df_movies = df_movies.dropna(how="all")

# Escrevendo s3
df_movies.write \
    .mode("overwrite") \
    .format("parquet") \
    .save(target_movies)


# Liberando memória
del df_movies

# ------------------ Processo series.csv ------------------

# schema para a tabela series.csv
schema = StructType([
    StructField("id", StringType(), True),
    StructField("tituloPincipal", StringType(), True),
    StructField("tituloOriginal", StringType(), True),
    StructField("anoLancamento", IntegerType(), True),
    StructField("anoTermino", IntegerType(), True),
    StructField("tempoMinutos", IntegerType(), True),
    StructField("genero", StringType(), True),
    StructField("notaMedia", FloatType(), True),
    StructField("numeroVotos", IntegerType(), True),
    StructField("generoArtista", StringType(), True),
    StructField("personagem", StringType(), True),
    StructField("nomeArtista", StringType(), True),
    StructField("anoNascimento", IntegerType(), True),
    StructField("anoFalecimento", IntegerType(), True),
    StructField("profissao", StringType(), True),
    StructField("titulosMaisConhecidos", StringType(), True)
])

# Leitura do s3
df_series = spark.read.csv(input_series, header=True, sep="|", schema=schema)

# Renomeação e Remoção de linhas duplicatas/nulas
df_series = df_series.withColumnRenamed("tituloPincipal", "tituloPrincipal")
df_series = df_series.dropDuplicates()
df_series = df_series.dropna(how="all")

# Escreve no s3
df_series.write \
    .mode("overwrite") \
    .format("parquet") \
    .save(target_series)

job.commit()