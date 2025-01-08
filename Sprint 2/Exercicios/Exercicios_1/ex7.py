'''
Escreva um programa que lê 
o conteúdo do arquivo texto 
arquivo_texto.txt e imprime 
o seu conteúdo.
'''

arquivo = open('arquivo_texto.txt', 'r')

print(arquivo.read(), end='')
