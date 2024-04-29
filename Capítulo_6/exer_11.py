#Exer 11 - Faça um programa que peça ao usuário para digitar uma lista de números e que, em seguida, use filter() para retornar uma nova lista apenas com os números pares.

numeros = input("Digite nomes separados por espaços:\n").split()
numeros = list(map(lambda x: float(x),numeros))

print(numeros)

numeros_novos = list(filter(lambda x: x%2==0,numeros))

print(numeros_novos)

