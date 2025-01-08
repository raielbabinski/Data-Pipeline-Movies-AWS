"""
Escreva uma função que recebe uma lista e retorna
uma nova lista sem elementos duplicados. Utilize 
a lista a seguir para testar sua função.

['abc', 'abc', 'abc', '123', 'abc', '123', '123']
"""

a = ['abc', 'abc', 'abc', '123', 'abc', '123', '123']

def removerDuplicatas(lista:list) -> list:
    RMDuplicatas = list(set(lista))
    return RMDuplicatas
       
print(removerDuplicatas(a))
