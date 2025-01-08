'''
Crie uma classe  Calculo que contenha
um método queaceita dois parâmetros, 
X e Y, e retorne a soma dos dois. Nessa 
mesma classe, implemente um método de 
subtração, que aceita dois parâmetros, 
X e Y, e retorne a subtração dos dois 
(resultados negativos são permitidos).
'''

class Calculo:

    def soma(x, y):
        return x + y
    
    def subtracao(x, y):
        return x - y
    
x = 4
y = 5

print(f'Somando: 4+5 = {Calculo.soma(x, y)}')
print(f'Sobtraindo: 4-5 = {Calculo.subtracao(x, y)}')
