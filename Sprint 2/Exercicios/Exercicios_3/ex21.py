'''
Utilizando high order functions, 
implemente o corpo da função conta_vogais. 
O parâmetro de entrada será uma string e 
o resultado deverá ser a contagem de vogais 
presentes em seu conteúdo.
'''

def conta_vogais(texto:str)-> int:
    vogais = filter(lambda char : char.lower() in 'aeiou', texto)
    return len(list(vogais))
