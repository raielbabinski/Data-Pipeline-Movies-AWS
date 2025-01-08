'''
Crie uma classe Ordenadora que contenha
um atributo listaBaguncada e que contenha 
os métodos ordenacaoCrescente e ordenacaoDecrescente.

Instancie um objeto chamado crescente dessa
classe Ordenadora que tenha como listaBaguncada
a lista [3,4,2,1,5] e instancie um outro 
objeto, decrescente dessa mesma classe com uma 
outra listaBaguncada sendo [9,7,6,8].

Para o primeiro objeto citado, use o método 
ordenacaoCrescente e para o segundo objeto, 
use o método ordenacaoDecrescente.
'''

class Ordenadora:
    def __init__(self, listaBaguncada:list):
        self.listaBaguncada = listaBaguncada

    def ordenacaoCrescente(self):
        self.listaBaguncada.sort()
        return self.listaBaguncada

    def ordenacaoDecrescente(self):
        self.listaBaguncada.sort(reverse=True)
        return self.listaBaguncada

crecente = Ordenadora([3,4,2,1,5])
decrecente = Ordenadora([9,7,6,8])


print(crecente.ordenacaoCrescente())
print(decrecente.ordenacaoDecrescente())
