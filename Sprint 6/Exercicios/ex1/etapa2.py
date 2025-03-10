'''
Em Python, declare e inicialize uma 
lista contendo o nome de 20 animais. 
Ordene-os em ordem crescente e itere 
sobre os itens, imprimindo um a um 
(pode utilizar list comprehension). 
Na sequência, armazene o conteúdo da 
lista em um arquivo de texto, um item 
em cada linha.
'''
animais = [
    "Tyrannosaurus Rex", "Velociraptor", "Triceratops", "Brachiosaurus", "Stegosaurus",
    "Spinosaurus", "Ankylosaurus", "Allosaurus", "Pachycephalosaurus", "Iguanodon",
    "Carnotaurus", "Dilophosaurus", "Parasaurolophus", "Therizinosaurus", "Diplodocus",
    "Giganotosaurus", "Deinonychus", "Compsognathus", "Stygimoloch", "Megalosaurus"
]

for dinossauro in sorted(animais):
    print(dinossauro)

with open("animais.txt", "a") as file:
    for dinossauro in animais:
        file.write(f"{dinossauro} \n")
