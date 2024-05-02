#Exer 2 - Crie um programa que leia um arquivo de texto e exiba quantas linhas ele possui.

arquivo = open("arquivo.txt","r")
linhas = arquivo.readlines()
contador = 0
for linha in linhas:
    contador+=1

print(f'Quantidade de linhas do arquivo: {contador}')

arquivo.close()