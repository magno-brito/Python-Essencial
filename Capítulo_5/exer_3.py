#Exer 3 : Crie uma função que tenha 3 parâmetros: um número inteiro, um número real e um texto. A função deve imprimir os valores dos parâmetros na tela. EM seguida, chame a função passando os argumentos de forma posicional.

def exer_3(numero_inteiro: int, numero_real: float, texto: str) -> None:
    print(f"Número inteiro: {numero_inteiro}, Número real: {numero_real} e Texto: '{texto}'")

exer_3(1,3.14,"Olá mundo")