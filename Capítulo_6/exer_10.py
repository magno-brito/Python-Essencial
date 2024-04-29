#Exer 10 - Faça um programa que peça ao usuário para digitar uma lista de palavras e que, em seguida, use map() para retornar uma nova lista com os comprimentos de todas as palavras.
#Exer 9 - Faça um programa que peça ao usuário para digitar uma lista de nomes e que em seguida use mapeamento map() para retornar uma nova lista com os nomes em caixa alta.

nomes = input("Digite nomes separados por espaços:\n").split()
print(nomes)

lista = list(map(lambda x: len(x), nomes))
print(lista)