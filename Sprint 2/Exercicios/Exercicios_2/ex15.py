'''
Implemente duas classes, Pato e Pardal, 
que herdam de uma superclasse chamada 
Passaro as habilidades de voar e emitir som.

Contudo, tanto Pato quanto Pardal devem emitir 
sons diferentes (de maneira escrita) no console, 
conforme o modelo a seguir.
'''

class Passaro:
    def voar(self):
        print("Voando...")

    def emitir_som(self):
        pass

class Pato(Passaro):
    def emitir_som(self):
        print('Quack Quack')

class Pardal(Passaro):
    def emitir_som(self):
        print('Piu Piu')


pato = Pato()
print('Pato')
pato.voar()
print('Pato emitindo som...')
pato.emitir_som()

pardal = Pardal()
print('Pardal')
pardal.voar()
print('Pardal emitindo som...')
pardal.emitir_som()
