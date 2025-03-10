from pyspark.sql import SparkSession
from pyspark import SparkContext, SQLContext
from pyspark.sql.functions import *
import random

# Etapa 1 ---------------------------------------------
'''
Nesta etapa, adicione código para ler o 
arquivo nomes_aleatorios.txt através do 
comando spark.read.csv.

Carregue-o para dentro de um dataframe 
chamado df_nomes e, por fim, liste 
algumas linhas através do método show.
'''

spark = SparkSession \
	.builder \
	.master("local[*]") \
	.appName("Exercicio Intro") \
	.getOrCreate()

df_nomes = spark.read.csv("nomes_aleatorios.txt")
df_nomes.show(5)

# Etapa 2 ---------------------------------------------
'''
Nesta etapa, será necessário adicionar 
código para renomear a coluna para 
"Nomes", imprimir o esquema e mostrar 
10 linhas do DataFrame.
'''

df_nomes = df_nomes.withColumnRenamed("_c0", "Nomes")

df_nomes.printSchema()
df_nomes.show(10)

# Etapa 3 ---------------------------------------------
'''
Ao DataFrame df_nomes, adicione uma 
nova coluna chamada "Escolaridade"
e atribua para cada linha um dos 
três valores de forma aleatória: 
"Fundamental", "Médio" ou "Superior". 
Para esta etapa, evite usar funções 
de iteração, como por exemplo: for, 
while, entre outras. Dê preferência 
aos métodos oferecidos pelo próprio 
Spark.
'''


escolaridade = ["Fundamental", "Medio", "Superior"]

# Cria coluna com ids aleatórios
df_nomes = df_nomes.withColumn("Escolaridade", rand()*3)

# Adiciona aleatóriamente uma escolaridade na coluna
df_nomes = df_nomes.withColumn(
		"Escolaridade", 
		when(df_nomes["Escolaridade"] < 1, escolaridade[0]) \
		.when((df_nomes["Escolaridade"] >= 1) & (df_nomes["Escolaridade"] < 2), escolaridade[1])\
		.when(df_nomes["Escolaridade"] >= 2, escolaridade[2])
)

df_nomes.show(10)

# Etapa 4 ----------------------------------------------
'''
Ao DataFrame df_nomes, adicione 
uma nova coluna chamada "País" 
e atribua para cada linha o 
nome de um dos 13 países da 
América do Sul, de forma 
aleatória. Para esta etapa, 
evite usar funções de iteração, 
como por exemplo: for, while, 
entre outras. Dê preferência aos 
métodos oferecidos pelo próprio 
Spark.
'''

america_sul = [
    (0 , "Argentina"), 
    (1 ,"Bolivia"), 
    (2 ,"Brasil"), 
    (3 ,"França_Guyana"),
    (4 ,"Chile"), 
    (5 ,"Colombia"), 
    (6 ,"Ecuador"), 
    (7 ,"Guyana"), 
    (8 ,"Paraguay"), 
    (9 ,"Peru"), 
    (10 ,"Suriname"), 
    (11 ,"Uruguay"), 
    (12 ,"Venezuela")   
]

# Cria um novo dataframe com os países
paises = spark.createDataFrame(america_sul, ["Indice","Pais"])

# Cria um id aleatório para cada país
df_nomes = df_nomes.withColumn("id_pais", (rand()*13).cast("int"))

# Faz o join entre as duas tabelas
df_nomes = df_nomes.join(paises, df_nomes.id_pais == paises.Indice, "inner")

df_nomes = df_nomes.drop("id_pais", "Indice")

df_nomes.orderBy("Nomes").show()

# Etapa 5 ------------------------------------
'''
Ao DataFrame [df_nomes], adicione uma nova 
coluna chamada AnoNascimento e atribua para 
cada linha um valor de ano entre 1945 e 
2010, de forma aleatória. Para esta etapa, 
evite usar funções de iteração, como por 
exemplo: for, while, entre outras. Dê 
preferência aos métodos oferecidos pelo 
próprio Spark.
'''

df_nomes = df_nomes.withColumn("AnoNascimento", (rand() * 66 + 1945).cast("int"))

df_nomes.show(40)

# Etapa 6 ------------------------------------------
'''
Usando o método select do DataFrame [df_nomes], 
selecione as pessoas que nasceram neste século.
Armazene o resultado em outro DataFrame 
chamado df_select e mostre 10 nomes deste.
'''
df_select = df_nomes.select("Nomes").where(column("AnoNascimento") >= 2000)

df_select.show(10)

# Etapa 7 ----------------------------------------
'''
Usando [Spark SQL], repita o processo 
da etapa 6. Lembre-se que, para 
trabalharmos com [Spark SQL], precisamos 
registrar uma tabela temporária e depois 
executar o comando [SQL]. 
'''

df_nomes.createOrReplaceTempView("pessoas")

spark.sql("select * from pessoas").show()

# Etapa 8 ---------------------------------------
"""
Usando o método filter do DataFrame 
[df_nomes], conte o número de pessoas 
que são da geração Millennials 
(nascidos entre 1980 e 1994) no 
Dataset.
"""

qtd = df_nomes \
    .filter(
        (df_nomes["AnoNascimento"] >= 1980) & (df_nomes["AnoNascimento"] <= 1994)
    ).count()

print(qtd)

# Etapa 9 ----------------------------------------
'''
Repita o processo da etapa 8 utilizando Spark SQL
'''
query = """

SELECT COUNT(*) AS total
FROM pessoas
WHERE AnoNascimento BETWEEN 1980 AND 1994;
"""

spark.sql(query).show()

# Etapa 10 ----------------------------------------
'''
Usando [Spark SQL], obtenha a quantidade 
de pessoas de cada país para cada uma das 
gerações abaixo. Armazene o resultado em 
um novo DataFrame e depois mostre todas 
as linhas em ordem crescente de País, 
Geração e Quantidade:

Baby Boomers — nascidos entre 1944 e 1964;

Geração X — nascidos entre 1965 e 1979;

Millennials (Geração Y) — nascidos entre 1980 e 1994;

Geração Z — nascidos entre 1995 e 2015.
'''


query = """
SELECT Pais, 'Baby Boomers' AS Geracao, COUNT(*) AS qtd
FROM pessoas
WHERE AnoNascimento >= 1944 AND AnoNascimento <= 1964
GROUP BY Pais

UNION ALL

SELECT Pais, 'Geração X' AS Geracao, COUNT(*) AS qtd
FROM pessoas
WHERE AnoNascimento >= 1965 AND AnoNascimento <= 1979
GROUP BY Pais

UNION ALL

SELECT Pais, 'Millennials' AS Geracao, COUNT(*) AS qtd
FROM pessoas
WHERE AnoNascimento >= 1980 AND AnoNascimento <= 1994
GROUP BY Pais

UNION ALL

SELECT Pais, 'Geração Z' AS Geracao, COUNT(*) AS qtd
FROM pessoas
WHERE AnoNascimento >= 1995 AND AnoNascimento <= 2015
GROUP BY Pais

ORDER BY Pais, Geracao;
"""

spark.sql(query).show()