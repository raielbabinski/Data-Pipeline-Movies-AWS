import sys
from awsglue.transforms import * # type: ignore
from awsglue.utils import getResolvedOptions # type: ignore
from pyspark.context import SparkContext # type: ignore
from awsglue.context import GlueContext # type: ignore
from awsglue.job import Job # type: ignore
from pyspark.sql.functions import *

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME','S3_INPUT_PATH', 'S3_TARGET_PATH'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

source_file = args['S3_INPUT_PATH']
target_path = args['S3_TARGET_PATH']

# Ler o arquivo nomes.csv no S3 (lembre-se de realizar upload do arquivo antes)

dynamic_frame = glueContext.create_dynamic_frame.from_options(
    connection_type="s3",  
    connection_options={
        "paths": [source_file]
    },
    format="csv",  
    format_options={"withHeader": True, "separator": ","} 
)

# Imprimir o schema do dataframe gerado no passo anterior.

dynamic_frame.printSchema()

# Escrever o código necessário para alterar a caixa dos valores da coluna nome para MAIÚSCULO

df = dynamic_frame.toDF()
df = df.withColumn("nome", upper(col("nome")))
df.show(5)

# Imprimir a contagem de linhas presentes no dataframe

qtd = df.count()
print(qtd)

# Imprimir a contagem de nomes, agrupando os dados do dataframe pelas colunas ano e sexo.
# Ordene os dados de modo que o ano mais recente apareça como primeiro registro do
# dataframe.

df.groupBy("ano", "sexo") \
    .agg(count(col('nome'))) \
    .orderBy(desc(col("ano"))) \
    .show(20)

# Apresentar qual foi o nome feminino com mais registros e em que ano ocorreu. 

df.filter(col("sexo") == "F") \
    .orderBy(desc("total")) \
    .select("nome", "ano", "total") \
    .show(1)
    
# Apresentar qual foi o nome masculino com mais registros e em que ano ocorreu. 

df.filter(col("sexo") == "M") \
    .orderBy(desc("total")) \
    .select("nome", "ano", "total") \
    .show(1)
    
# Apresentar o total de registros (masculinos e femininos) 
# para cada ano presente no dataframe.
# Considere apenas as primeiras 10 linhas, 
# ordenadas pelo ano, de forma crescente. 

df.groupBy("ano").count().orderBy(desc(col("ano"))).show(10)

# Escrever o conteúdo do dataframe com os valores de nome em maiúsculo no S3. 

df.write \
    .mode("overwrite") \
    .format("json") \
    .partitionBy("sexo", "ano") \
    .save(target_path)


job.commit()