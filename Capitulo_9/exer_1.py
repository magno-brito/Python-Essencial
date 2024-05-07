#Exer 1 -> Crie um programa que solicite ao usuário  dois números inteiros e exiba a divisão do primeiro número pelo segundo. Trate possíveis exceções de divisão por zero. 

try:
    numero_a = float(input("Digite um número:\n"))
    numero_b = float(input("Digite um segundo número:\n"))
    print(f'{numero_a} / {numero_b} = {numero_a/numero_b}')
except:
    print("Não é possível divisão por zero.")