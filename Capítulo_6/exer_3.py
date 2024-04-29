#Exer 3 - Faça um programa que use list comprehension para criar uma lista com o quadrado dos números pares entre 0 e 10.

lista = [x**2 for x in range(11) if x%2 == 0]
print(lista)