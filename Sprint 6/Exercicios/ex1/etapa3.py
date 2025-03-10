import random
import names
import os
import time

"""
Elabore um código em Python
para gerar um dataset de 
nomes de pessoas. Siga estes
passos a seguir para realizar 
a atividade.
"""


random.seed(40)

qtd_nomes_unicos = 39080

qtd_nomes_aleatorios = 10000000

aux = []

for i in range(0, qtd_nomes_unicos):
    aux.append(names.get_full_name())

print(f'Gerando {qtd_nomes_aleatorios} nomes aleatórios')

dados = []
for i in range(0, qtd_nomes_aleatorios):
    dados.append(random.choice(aux))

with open("nomes_aleatorios.txt", "a") as file:
    for nome in dados:
        file.write(f"{nome} \n")