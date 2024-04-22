#Exer 1 - Crie um programa que mostre todos os números de 1 a 100

def exer_1():
    for i in range(1,101):
        print(i, end=" ")

#Exer 2 - Cire um programa que mostre todos os números pares de 1 a 100

def exer_2(): 
    for i in range(1,101):
        if i%2 == 0:
            print(i, end=" ")

#Exer 3 - Crie um programa que mostre todos os números ímpares de 1 a 100

def exer_3():
    for i in range(1,101):
        if i%2 != 0:
            print(i, end=" ")

#Exer 4 - Crie um programa que some e mostre todos os números de 1 a 100

def exer_4():
    soma = 0
    for i in range(1,101):
        print(i, end=" ")
        soma += i
    print(" ")
    print("Soma de todos os números: " + str(soma))


#Exer 5 - Crie um programa que some e mostre todos os números pares de 1 a 100

def exer_5():
    soma = 0
    for i in range(1,101):
        if i%2 == 0:
            print(i, end=" ")
            soma += i
    print(" ")
    print("Soma de todos os números pares: " + str(soma))


#Exer 6 - Crie um programa que some e mostre todos os números ímpares de 1 a 100

def exer_6():
    soma = 0
    for i in range(1,101):
        if i%2 != 0:
            print(i, end=" ")
            soma += i
    print(" ")
    print("Soma de todos os números ímpares: " + str(soma))

#Exer 7 - Crie um programa que leia vários números positivos digitados pelo usuário, até que ele digite um valor negativo. Ao fim, o programa deve mostrar a média dos números positivos digitados. 

def exer_7():
    soma_positivos = 0
    while True:
        entrada = float(input("Digite um número:\n"))
        if entrada > 0:
            soma_positivos += entrada
        elif entrada < 0:
            break
    print("Soma dos números positivos digitados: " + str(soma_positivos))

#Exer 8 - Crie um programa que calcule e mostre o fatorial de um número digitado pelo usuário.

def exer_8():
    numero = int(input("Digite um número natural: \n"))
    fatorial = 1
    for i in range(numero,1,-1):
        fatorial *=i
    print("Fatorial do número: " + str(fatorial))

#Exer 9 - Crie um programa que calcule e mostre todos os números divisíeis por 3 e 5 de 1 a 100.

def exer_9():
    for i in range(1, 101):
        if i%15 == 0:
            print(i, end= " ")

#Exer 10 - Crie um programa que calcule e mostre todos os números primos de 1 a 100.

def exer_10():
    for i in range(1, 101):
        primo = True
        for k in range(2, i):
            if i%k == 0:
                primo = False
        if primo:
            print(str(i) + ", ", end = "")

#Exer 11 - Crie um programa que calcule e mostre todos os números entre 1 e 100 que possuem raiz quadrada exata.

def exer_11():
    for i in range(1, 101):
        if (i**(1/2))%2 == 0:
            print(str(i) + ", ", end="")

#Exer 12 - Crie um programa que calcule e mostre a soma de todos os números primos de 1 a 100.

def exer_12():
    soma = 0
    for i in range(2, 101):
        primo = True
        for k in range(2, i):
            if i%k == 0:
                primo = False
        if primo:
            soma += i
            print(i)
            print("Soma ->" + str(soma) + ", ")

#Exer 13 - Crie um programa que calcule e mostre a tabuada de um número digitado pelo usuário.

def exer_13():
    numero = int(input("Digite um número natural:\n"))
    for i in range(1,11):
        tabuada = numero*i
        print(f'{i} X {numero} = {tabuada}')

#Exer 14 - Crie um programa que verifique se um número digitado pelo usuário é primo.

def exer_14():
    numero = int(input("Digite um número natural: \n"))
    primo = True
    for i in range(2, numero):
        if numero%i == 0:
            primo = False
    if primo:
        print("É um número primo")
    else:
        print("Não é primo")

#Exer 15 - Crie um programa que verifique se um número digitado pelo usuário é perfeito.

def exer_15():
    numero = int(input("Digite um número natural: \n"))
    divisores = list()
    for i in range(1, numero):
        if numero%i == 0:
            divisores.append(i)
    
    soma = 0
    for i in divisores:
        soma += i
    if soma == numero:
        print("Número perfeito")
    else:
        print("Número não é perfeito")

#-----------------------------------------------------------
#Chamando a função

exer_15()
