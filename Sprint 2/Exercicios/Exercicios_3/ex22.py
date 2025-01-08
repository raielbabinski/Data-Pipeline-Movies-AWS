'''
A função calcula_saldo recebe uma 
lista de tuplas, correspondendo a 
um conjunto de lançamentos bancários. 
Cada lançamento é composto pelo seu 
valor (sempre positivo) e pelo seu 
tipo (C - crédito ou D - débito). 
'''

from functools import reduce

def calcula_saldo(lancamentos) -> float:
    lanc = tuple(map(lambda lancamento : lancamento[0] if lancamento[1] == 'C' else -lancamento[0], lancamentos))
    saldo = reduce(lambda a, b : a + b, lanc, 0)
    return saldo
