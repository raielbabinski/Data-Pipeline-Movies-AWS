'''
Implemente a classe Lampada. A classe 
Lâmpada recebe um booleano no seu construtor, 
Truese a lâmpada estiver ligada, False caso 
esteja desligada. A classe Lampada possuí 
os seguintes métodos:

liga(): muda o estado da lâmpada para ligada

desliga(): muda o estado da lâmpada para desligada

esta_ligada(): retorna verdadeiro se a lâmpada
estiver ligada, falso caso contrário
'''

class Lampada:
    def __init__(self, estado=False):
        self.ligada = estado
    
    def liga(self):
        self.ligada = True

    def desliga(self):
        self.ligada = False

    def esta_ligada(self):
        if self.ligada:
            return True
        else:
            return False
        
if __name__ == '__main__':
    lampada = Lampada(True)
    print(f'A lâmpada está ligada?{lampada.esta_ligada()}')
    
    lampada.desliga()
    print(f'A lâmpada está ligada?{lampada.esta_ligada()}')
    