'''
Escreva uma função que recebe 
como parâmetrouma lista e retorna 
3 listas: a lista recebida dividida 
em 3 partes iguais. Teste sua 
implementação com a lista abaixo
'''

def separacao_lista(lista:list):
    lista_dividida = []
    divisao = []
    tamanho_divisao = len(lista)/3

    for num in lista:
        divisao.append(num)
        
        if len(divisao) == tamanho_divisao:
            lista_dividida.append(divisao)
            divisao = []

    return lista_dividida
    
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
lista_separada = (separacao_lista(lista))
for i in range(len(lista_separada)):
    if i == len(lista_separada)-1:
        print(f'{lista_separada[i]}')
    else:
        print(f'{lista_separada[i]} ', end = '')
