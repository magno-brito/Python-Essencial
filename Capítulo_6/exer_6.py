#Exer 6 - Faça um programa que use dict comprehension para criar um dicionário com as raízes quadradas de números de 1 a 100. Utilize os números como chave e as raízes como o valor.

dicionario = {x:round(x**(1/2),3) for x in range(11) }
print(dicionario)