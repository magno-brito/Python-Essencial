#Exer 1 - Crie um programa que solicite ao usuário um nome de arquivo e que exiba seu conteúdo na tela.

arquivo = open("arquivo.txt","r")
linhas = arquivo.readlines()
for i in linhas:
    print(i, end="")

arquivo.close()