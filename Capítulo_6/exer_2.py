#Exer 2 - Faça um programa que use list comprehension para criar uma lista com as palavras contêm "a" em uma frase digitada pelo usuário, substituindo a letra "o".


def exer_2(frase: str) -> list:
    frase_split = frase.split()
    frase_split = [ i.lower() for i in frase_split]
    lista = [termo.replace("a", "o") for termo in frase_split if "a" in termo ]
    return lista

frase = "A casa eve asa"
print(exer_2(frase))