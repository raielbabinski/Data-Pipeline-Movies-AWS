'''
Escreva uma função que recebe
uma string de números separados
por vírgula e retorne a soma
de todos eles. Depois imprima 
a soma dos valores.
'''

def soma_string(string_somar:str):
    lista_numero = string_somar.split(',')
    resultado = 0

    for num_string in lista_numero:
        resultado += int(num_string)

    return str(resultado)    

if __name__ == '__main__':
    print(soma_string("1,3,4,6,10,76"))
