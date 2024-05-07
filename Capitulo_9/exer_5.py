#Exer 5 -> Crie uma função que leia um arquivo de texto e exiba o conteúdo na tela. Trate exceções caso o arquivo não exista ou seja possível le-lo.

def ler_arquivo(arquivo):
    try:
        file = open(arquivo,"r")
        linhas = file.readlines()
        for i in linhas:
            print(i)
    except FileNotFoundError:
        print("Arquivo não encontrado!")

print("--------------------")
ler_arquivo("arquio.txt")
print("--------------------")
ler_arquivo("arquivo.txt")