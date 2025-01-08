'''
Escreva uma função que recebe 
um número variável de parâmetros 
não nomeados e um número variado 
de parâmetros nomeados e imprime 
o valor de cada parâmetro recebido.
'''

def teste(*args, **kvargs):
    for i in args:
        print(i)
    for i in kvargs.values():
        print(i)

teste(1, 3, 4, 'hello', parametro_nomeado='alguma coisa', x=20)
