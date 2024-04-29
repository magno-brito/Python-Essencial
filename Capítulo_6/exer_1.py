#Exer 1 - Faça um programa que use list comprehension para criar uma lista com as raízes quadradas dos números pares de 0 a 20

lista = [p**(1/2) for p in range(21) if p%2 == 0]
print(lista)