'''
Você foi encarregado de desenvolver uma 
nova feature  para um sistema de gestão 
de supermercados. O analista responsável 
descreveu o requisito funcional da seguinte 
forma:

- Para realizar um cálculo de custo, o sistema 
deverá permitir filtrar um determinado conjunto 
de produtos, de modo que apenas aqueles cujo 
valor unitário for superior à média deverão estar 
presentes no resultado. Vejamos o exemplo:
'''

def maiores_que_media(conteudo:dict)->list:
    media = sum(conteudo.values())/ len(conteudo) 
    lista_maior_media = []
    for key, item in conteudo.items():
        if item > media:
            lista_maior_media.append((key, item))
    lista_maior_media = sorted(lista_maior_media, key=lambda x : x[1])
    return lista_maior_media
    