'''
Um determinado sistema escolar exporta 
a grade de notas dos estudantes em 
formato CSV. Cada linha do arquivo 
corresponde ao nome do estudante, 
acompanhado de 5 notas de avaliação, 
no intervalo [0-10]. É o arquivo 
estudantes.csv de seu exercício.
'''

def organiza(estudante:str):
    lista_notas = estudante.split(',')
    nome = lista_notas.pop(0)
    lista_notas = list(map(lambda nota : int(nota), lista_notas))
    lista_notas = sorted(lista_notas, reverse=True)
    lista_notas = lista_notas[0:3]
    lista_notas.insert(0, nome)
    return lista_notas

with open('estudantes.csv') as estudantes:
    estudantes = open('estudantes.csv')
    lista_estudantes = list(map(organiza, estudantes))

lista_estudantes = sorted(lista_estudantes, key=lambda x : x[0] )

for estudante in lista_estudantes:
    print(f'Nome: {estudante[0]} Notas: {estudante[1:4]} Média: {round(sum(estudante[1:4])/3, 2)}')
