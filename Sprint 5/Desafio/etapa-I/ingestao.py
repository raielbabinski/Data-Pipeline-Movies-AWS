import boto3
import os

# Cliente s3
s3 = boto3.client("s3")

# Informações do bucket
bucket = "data-lake-raiel"
s3_movie = "Raw/local/CSV/Movies/2025/02/21/movies.csv"
s3_series = "Raw/local/CSV/Series/2025/02/21/series.csv"

# Upload do arquivo
s3.upload_file("movies.csv", bucket, s3_movie)
s3.upload_file("series.csv", bucket, s3_series)

print("Upload feito com sucesso!")