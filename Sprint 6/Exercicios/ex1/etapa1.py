import random

"""
Declare e inicialize uma lista 
contendo 250 números inteiros 
obtidos de forma aleatória. 
Após, aplique o método reverse 
sobre o conteúdo da lista e 
imprima o resultado.
"""

random_num = []

for i in range(0, 250):
    random_num.append(random.randint(0,10000))

random_num.reverse()
print(random_num)