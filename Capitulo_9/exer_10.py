#Exer 10 -> Crie uma função chamada importar_modulo que recebe o nome de um arquivo módulo como argumento e tenta importá-lo. A função deve usar um bloco para tratar a exceção ModuleNotFoundError caso o módulo não exista. Se a importação for bem sucedida, a função deve imprimir uma mensagem dizendo que o módulo foi importado com sucesso. Caso contrário, deve imprimir uma mensagem informando que o módulo não foi encontrado. Independentemente de ocorrer ou não uma exceção, a função deve imprimir "Operação finalizada" ao final.

def importar_modulo(nome_modulo):
    try:
        __import__(nome_modulo)
        print("Módulo importado")
    except ModuleNotFoundError:
        print("Módulo não encontrado")
    finally:
        print("Operação finalizad!")

modulo = "math"
importar_modulo(modulo)
