'''
Generators são poderosos recursos 
da linguagem Python. Neste exercício, 
você deverá criar o corpo de uma função, 
cuja assinatura já consta em seu arquivo 
de início (def pares_ate(n:int):) .

O objetivo da função pares_ate é retornar 
um generator para os valores pares no intervalo 
[2,n] . Observe que n representa o valor do 
parâmetro informado na chamada da função.
'''

def pares_ate(n:int):
    retorno = 0
    while n != retorno:
        retorno += 2
        yield retorno 