"""
Verifique se cada uma das palavras da lista
['maça', 'arara', 'audio', 'radio', 'radar', 'moto']
é ou não um palíndromo.

Obs: Palíndromo é uma palavra que permanece igual se lida de 
traz pra frente.
"""

words = ['maça', 'arara', 'audio', 'radio', 'radar', 'moto']

for word in words:
    reverse = word[::-1]
    if reverse == word:
        print("A palavra:", word, "é um palíndromo\n")
    else:
        print("A palavra:", word, "não é um palíndromo\n")
