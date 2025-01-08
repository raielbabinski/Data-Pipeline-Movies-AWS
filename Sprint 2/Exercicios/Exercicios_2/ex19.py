'''
Crie uma classe Avião que possua
os atributos modelo, velocidade_maxima, 
cor e capacidade.

Defina o atributo cor de sua classe , 
de maneira que todas as instâncias de 
sua classe avião sejam da cor “azul”.

Após isso, a partir de entradas abaixo, 
instancie e armazene em uma lista 3 
objetos da classe Avião.

Ao final, itere pela lista imprimindo 
cada um dos objetos no seguinte formato:

“O avião de modelo “x” possui uma 
velocidade máxima de “y”, capacidade 
para “z” passageiros e é da cor “w”.

Sendo x, y, z e w cada um dos atributos da classe “Avião”.
'''

class Aviao:
    def __init__(self, modelo, velocidade_maxima, capacidade):
        self.modelo = modelo
        self.velocidade_maxima = velocidade_maxima
        self.cor = 'azul'
        self.capacidade = capacidade


boieng456 = Aviao('BOIENG456', 1500, 400)
embraer_praetor = Aviao('Embraer Praetor 600', 863, 14)
antonov_an2 = Aviao('Antonov An-2', 258, 12)

lista_avioes = [boieng456, embraer_praetor, antonov_an2]

for aviao in lista_avioes:
    print(f'O avião de modelo {aviao.modelo} possui uma velocidade máxima de {aviao.velocidade_maxima}, capacidade para {aviao.capacidade} passageiros e é da cor {aviao.cor}')
