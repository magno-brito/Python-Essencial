#Exer 1: Crie um programa que verifique se um número é par ou ímpar

def exer_1():
    numero = int(input("Digite um número:\n"))
    if numero%2 == 0:
        print("Número par")
    else:
        print("Número ímpar")

#Exer 2: Crie um programa que verifique se um número digitado pelo usuário é positivo, negativo ou zero.
def exer_2():
    numero = int(input("Digite um número:\n"))
    if numero > 0:
        print("Número positivo")
    elif numero < 0:
        print("Número negativo")
    else:
        print("Número é igual a 0")

#Exer 3: Crie um programa que verifique se uma letra digitada pelo usuário é uma vogal ou consoante.
def exer_3():
    vogais = ['A', 'E', 'I','O','U']
    letra = input("Digite uma letra:\n")
    if letra.upper() in vogais:
        print("Vogal")
    else:
        print("Consoante")

#Exer 4: Crie um programa que verifique se um ano é bissexto ou não.
def exer_4():
    ano = int(input("Digite um ano:\n"))

    if ano%100 == 0:
        if ano%400 == 0:
            print("É ano bissexto")
        else:
            print("Não é bissexto")
    else:
        if ano%4 == 0:
            print("É bissexto")
        else:
            print("Não é bissexto")

#Exer 5: Crie um programa que, a partir da idade digitada pelo usuário, verifique se ele é maior de idade ou não.
def exer_5():
    idade = int(input("Digite sua idade:\n"))
    if idade >= 18:
        print("Maior de idade")
    elif idade < 0:
        print("Não existe idade negativa")
    else:
        print("Menor de idade")

#Exer 6: Crie um programa que verifique se um texto digitado pelo usuário é um palíndromo ou não (uses texto[::-1] para obter o texto invertido)
def exer_6():
    texto = input("Digite uma palavra:\n")
    texto = texto.lower()
    if texto == texto[::-1]:
        print("É um palíndromo")
    else:
        print("Não é um palíndromo")

#Exer 7: Crie um programa que verifique se um texto digitado pelo usuário é um número inteiro ou não e mostre uma mensagem de acordo (use texto.isdigit() para verificar)
def exer_7():
    print("ok")

#Exer 8: Crie um programa que verifique se um texto digitado pelo usuário corresponde a uma data no formato "dd/mm/aaaa", considerando que a data deve ter 10 caracteres, "dd" deve variar de 01 a 31, "mm" de 01 a 12 e "aaaa" de 0001 a 9999. Utilize colchetes para acessar os caracteres do texto pelo seu índice (exemplos: texto[0:2] )
def exer_8():
    print("ok")

#Exer 9: Crie um programa que calcule a média de três números e exiba a mensagem "Aprovado" se for maior ou igual a 6 ou "Reprobado" caso contrário. Se a nota for 10 exiba parabéns. 
def exer_9():
    print("ok")

#Exer 10: Crie um programa que verifique se uma temperatura corporal digitada pelo usuário está acima, abaixou ou dentro da faixa normal (36°C a 37°C)
def exer_10():
    print("ok")

#Exer 11: Crie um programa que verifique se uma pessoa pode votar ou não, considerando sua idade e sua nacionalidade, digitadas pelo usuário (se tem 16 anos ou mais e é brasileiro)
def exer_11():
    print("ok")

#Exer 12: Crie um programa que verifique se uma pessoa é elegível para aposentadoria (se tem 60 anos ou mais para mulheres ou 65 anos para homens). O usuário deve digitar a idade e o gênero da pessoa a ser verificada.
def exer_12():
    print("ok")

#Exer 13: Crie um programa que verifique se um número inteiro digitado pelo usuário é divisível por outro número inteiro também digitado pelo usuário.
def exer_13():
    print("ok")

#Exer 14: Crie um programa que pergunte seu salário e exiba uma mensagem "Alto Salário" se o salário for maior que R$ 10.000,00 ou "Baixo Salário" caso contrátio.
def exer_14():
    print("ok")

#Exer 15: Crie um programa que peça ao usuário para digitar uma palavra. O programa deve então indicar se a palavra inserida começa com uma vogal ou com um consoante. 
def exer_15():
    print("ok")


#-----------------------------------------------------------
#Chamando a função

exer_6()
