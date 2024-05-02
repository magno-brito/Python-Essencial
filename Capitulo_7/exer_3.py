#Exer 3 - Crie um programa que leia um arquivo texto, inverta o conteúdo de cada linha e salve o resultado em um novo arquivo. 

with open('arquivo.txt') as arquivo:
    linhas = [line.rstrip() for line in arquivo]

print(linhas)
for i in range(len(linhas)):
    linhas[i] = linhas[i].split()[::-1]
for k in range(len(linhas)):
    juncao = ""
    for p in range(len(linhas[k])):
        juncao += linhas[k][p]+" "
    linhas[k] = juncao

novo_arquivo = open("novo_arquivo.txt","w")
for i in linhas:
    novo_arquivo.write(i + "\n")



