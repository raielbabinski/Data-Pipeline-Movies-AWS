'''
Leia o arquivo person.json, faça o parsing e imprima seu conteúdo
'''

import json

with open('person.json', 'r') as person:
    data = json.load(person) 
  
print(data)
