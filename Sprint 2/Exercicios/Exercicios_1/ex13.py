'''
Calcule o valor mínimo, 
valor máximo, valor médio 
e a mediana da lista gerada 
na célula abaixo:
'''

import random

random_list = random.sample(range(500), 50)
random_list.sort()

meio_random = (len(random_list)-1)/2

mediana = (random_list[int(meio_random)] + random_list[int(meio_random)+1])/2
media = sum(random_list)/len(random_list)
valor_minimo = min(random_list)
valor_maximo = max(random_list)

print(f'Media: {media}, Mediana: {mediana}, Mínimo: {valor_minimo}, Máximo: {valor_maximo}')
