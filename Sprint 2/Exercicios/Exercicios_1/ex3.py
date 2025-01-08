"""
Dada as listas a seguir:

primeirosNomes = ['Joao', 'Douglas', 'Lucas', 'José']
sobreNomes = ['Soares', 'Souza', 'Silveira', 'Pedreira']
idades = [19, 28, 25, 31]

Faça um programa que imprima o dados na 
seguinte estrutura: "índice - primeiroNome 
sobreNome está com idade anos".

"""

primeirosNomes = ['Joao', 'Douglas', 'Lucas', 'José']
sobreNomes = ['Soares', 'Souza', 'Silveira', 'Pedreira']
idades = [19, 28, 25, 31]

for i, _ in enumerate(primeirosNomes):
    print(f'{i} - {primeirosNomes[i]} {sobreNomes[i]} está com {idades[i]} anos')

