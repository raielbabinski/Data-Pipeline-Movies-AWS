'''
mplemente a função my_map(list, f) 
que recebe uma lista como primeiro
argumento e uma função como segundo
argumento. Esta função aplica a função
recebida para cada elemento da ]
lista recebida e retorna o resultado
em uma nova lista.mplemente a função 
my_map(list, f) que recebe uma lista 
como primeiro argumento e uma função 
como segundo argumento. Esta função aplica 
a função recebida para cada elemento da 
lista recebida e retorna o resultado em 
uma nova lista.
'''

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#power of two
def pot(num:int):
    num = num ** 2
    return num

def my_map(lista:list, f):
    for i, _ in enumerate(lista):
        lista[i] = f(lista[i])
    return lista
print(my_map(lista, pot))
