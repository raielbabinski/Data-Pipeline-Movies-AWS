import sys
from awsglue.transforms import * # type: ignore
from awsglue.utils import getResolvedOptions# type: ignore
from pyspark.context import SparkContext# type: ignore
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

df = spark.read.parquet(input_path)

# ----- Remoção e tratamento de dados -----

df = df.where(col("revenue") > 1)

df = df.drop(df["adult"])
df = df.drop(df["homepage"])
df = df.drop(df["belongs_to_collection"])
df = df.drop(df["imdb_id"])

df = df.withColumn("genres", expr("transform(genres, x -> x.name)"))
df = df.withColumn("genres", explode("genres"))

df = df.withColumn("origin_country", explode("origin_country"))

df = df.withColumn("production_companies", expr("transform(production_companies, x -> x.name)"))
df = df.withColumn("production_companies", explode("production_companies"))

df = df.withColumn("spoken_languages", explode("spoken_languages"))

df = df.withColumn("production_countries", explode("production_countries"))

# ----- Criação das dimensões -----

dim_filme = df.select(
	"id" , 
	"status",
	col("title").alias("titulo"),
	col("original_title").alias("titulo_original"),
	col("tagline").alias("slogan"),
	col("overview").alias("descricao")
).dropDuplicates()


dim_tempo = df.select(
	"release_date",
	year(col("release_date").alias("ano")),
	month(col("release_date").alias("mes")),
	day(col("release_date").alias("dia"))
).dropDuplicates()

dim_genero = df.select(
	col("genres").alias("genero")
).dropDuplicates()
dim_genero = dim_genero.withColumn("id_genero", monotonically_increasing_id())

dim_paises = df.select(
	col("production_countries").getField("name").alias("nome_pais"),
	col("production_countries").getField("iso_3166_1").alias("iso_pais"),
).dropDuplicates()
dim_paises = dim_paises.withColumn("id_pais", monotonically_increasing_id())


dim_produtora = df.select(
	col("production_companies").alias("nome_produtora")
).dropDuplicates()
dim_produtora = dim_produtora.withColumn("id_produtora", monotonically_increasing_id())


dim_linguagem = df.select(
	col("spoken_languages").getField("iso_639_1").alias("iso_linguagem"),
	col("spoken_languages").getField("english_name").alias("nome_lingua_en")
).dropDuplicates()
dim_linguagem = dim_linguagem.withColumn("id_linguagem", monotonically_increasing_id())

# ----- Criação da fato -----

fato_filme = df.select(
	col("id").alias("id_filme"),
	col("release_date").alias("data_lancamento"),
	col("budget").alias("orcamento"),
	col("revenue").alias("receita"),
	col("popularity").alias("popularidade"),
	col("runtime").alias("duracao"),
	col("vote_average").alias("media_votos"),
	col("vote_count").alias("quantidade_votos"),
	"genres",
	"production_companies",
	"origin_country",
	"original_language",
	"production_countries",
	"spoken_languages"
).dropDuplicates()

fato_filme = fato_filme.withColumn("lucro", col("receita") - col("orcamento"))

fato_filme = fato_filme.join(
	dim_genero, 
	fato_filme.genres == dim_genero.genero, 
	"inner"
).drop("genres", "genero")

fato_filme = fato_filme.join(
	dim_produtora, 
	fato_filme.production_companies == dim_produtora.nome_produtora, 
	"inner"
).drop("production_companies", "nome_produtora")

fato_filme = fato_filme.join(
	dim_paises, 
	fato_filme.origin_country == dim_paises.iso_pais, 
	"inner"
).drop("origin_country", "iso_pais", "nome_pais")

fato_filme = fato_filme.withColumnRenamed("id_pais", "id_pais_origem")

fato_filme = fato_filme.join(
	dim_paises, 
	fato_filme.production_countries.getField("name") == dim_paises.nome_pais, 
	"inner"
).drop("production_countries", "nome_pais", "iso_pais")

fato_filme = fato_filme.withColumnRenamed("id_pais", "id_paises_produção")

fato_filme = fato_filme.join(
	dim_linguagem, 
	fato_filme.original_language == dim_linguagem.iso_linguagem, 
	"inner"
).drop("iso_linguagem", "nome_lingua_en", "original_language")

fato_filme = fato_filme.withColumnRenamed("id_linguagem", "id_linguagem_original")

fato_filme = fato_filme.join(
	dim_linguagem, 
	fato_filme.spoken_languages.getField("name") == dim_linguagem.nome_lingua_en, 
	"inner"
).drop("iso_linguagem", "nome_lingua_en", "spoken_languages")

fato_filme = fato_filme.withColumnRenamed("id_pais", "id_paises_produção")

fato_filme = fato_filme.withColumn("id", monotonically_increasing_id())

# ----- Escrita das tabelas no S3 -----

def salvar_tabela(df, nome_tabela, path):
    df.write.mode("overwrite").format("parquet").save(f"{path}/{nome_tabela}")

# ----- Escrita das tabelas no S3 -----
salvar_tabela(dim_filme, "dim_filme", target_path)
salvar_tabela(dim_tempo, "dim_tempo", target_path)
salvar_tabela(dim_genero, "dim_genero", target_path)
salvar_tabela(dim_paises, "dim_paises", target_path)
salvar_tabela(dim_produtora, "dim_produtora", target_path)
salvar_tabela(dim_linguagem, "dim_linguagem", target_path)
salvar_tabela(fato_filme, "fato_filme", target_path)

job.commit()