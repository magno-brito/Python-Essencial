#Exer 9 -> Crie uma função chamada read_file que recebe o nome de um arquivo como argumento e imprime o conteúdo do arquivo. A função deve abrir o arquivo para leitura no bloco try, tratar exceções no bloco except para o caso do arquivo não existir, e finalmente fechar o arquivo no bloco finally, independente de exceções terem sido lançadas ou não. 

def read_file(arquivo):
    
    try:
        arquivo_aberto = open(arquivo, "r")
        linhas = arquivo_aberto.readlines()
        for linha in linhas:
            print(linha)
        arquivo_aberto.close()
    except FileNotFoundError as erro:
        raise ValueError("Erro ao ler arquivo")
    finally:
        print("Encerrado")
        
read_file("novo_arquivo.txt")
print("-------------------")
read_file("arqui.txt")