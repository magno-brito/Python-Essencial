#Exer 8 - Faça um programa que peça ao usuário para digitar uma lista de números e que use o (map()) para retornar uma nova lista com os quadrados de cada número.

def exer_8():
    numeros = input("Digite um lista de números separados por espaços em branco:\n").split()
    numeros = [float(i) for i in numeros]
   
    resultado = map(lambda x: x**2, numeros)
    print(list(resultado))

exer_8()

