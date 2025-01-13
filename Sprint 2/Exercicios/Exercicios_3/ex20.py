'''
Você está recebendo um arquivo contendo 
10.000 números inteiros, um em cada linha. 
Utilizando lambdas e high order functions, 
apresente os 5 maiores valores pares e a 
soma destes.
'''

with open('number.txt') as arquivo:
    arquivo = open('number.txt')
    numeros = map(lambda elemento: int(elemento), arquivo)

numeros_pares = list(filter(lambda numero: numero % 2 == 0, list(numeros)))
numeros_pares = sorted(numeros_pares, reverse=True)
print(numeros_pares[:5])
print(int(sum(numeros_pares[:5])))
