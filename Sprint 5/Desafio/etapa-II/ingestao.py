import requests
import boto3
import json
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Cria o cliente no s3
s3 = boto3.client("s3")

def lambda_handler(event, context):
    lista_ips = []
    json_load = {"movies": []}
    num = 1
    
    # Armazena total de páginas
    paginas = request_ips(1)["total_pages"]
    logger.info(f"Total de páginas: {paginas}")

    # Percore todas as páginas
    for pagina in range(1, paginas + 1):
        # Faz request do discover e armazena os ids.
        request_pagina = request_ips(pagina)
        for item in request_pagina["results"]:
            lista_ips.append(item["id"])

        # A cada 5 páginas faz a contrução do json e envia pro s3
        if (pagina % 5) == 0 or pagina == paginas:
            # Cria dict com as informações dos filmes
            for ip in lista_ips:
                movie = request_movie(ip)
                del movie["backdrop_path"]
                del movie["poster_path"]
                del movie["video"]
                json_load["movies"].append(movie)

            # Envia o json pro s3
            s3.put_object(
                Bucket="data-lake-raiel",
                Key=f"Raw/TMDB/JSON/Movies/2025/02/21/movies-{str(num).zfill(2)}.json",
                Body=json.dumps(json_load, indent=4)
            )

            # Limpa as variaveis para repetição do processo
            lista_ips.clear()
            json_load.clear()
            json_load["movies"] = []
            
            logger.info(f"json {num} enviado")
            num += 1

    return {"status": "Concluído", "arquivos_gerados": num - 1}

def request_ips(page):
# Requisições de IPs dos filmes na API

    url = f"https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=pt-BR&page={page}&release_date.lte=1990-01-01&sort_by=primary_release_date.asc&with_genres=27"
    return request(url)

def request_movie(ip):    
# Requisições das informações dos filmes por id

    url = f"https://api.themoviedb.org/3/movie/{ip}?language=en-US"
    return request(url)


def request(url):
# Faz as requisições

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer XXXXXXXXXXXXXXXX"
    }

    # Tratamento para uma possivel falha na requisição
    for i in range(2):
        try:
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                return response.json()
            else:
                print(f"Request {i}: Erro {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Request {i}: Erro na requisição ({e})")

    print("Erro na requisição")
    return {"erro": "Falha ao obter resposta da API"}
