'''
A função calcular_valor_maximo 
deve receber dois parâmetros, 
chamados de operadores e operandos. 
Em operadores, espera-se uma lista 
de caracteres que representam as 
operações matemáticas suportadas 
(+, -, /, *, %), as quais devem 
ser aplicadas à lista de operadores 
nas respectivas posições. Após 
aplicar cada operação ao respectivo 
par de operandos, a função deverá 
retornar o maior valor dentre eles.
'''

def calcular_valor_maximo(operadores,operandos) -> float:
    lista_val_op =  list(zip(operadores, operandos))
   
    valores_calc = map(
                        lambda tupla : 
                            eval(f'{tupla[1][0]} {tupla[0]} {tupla[1][1]}'), 
                        lista_val_op)
    
    return max(list(valores_calc))
