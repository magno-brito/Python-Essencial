import math
import re

#Exer 1 - Crie um programa que peça ao usuário para inserir dois números e calcule a potência do primeiro número pelo segundo

def exer_1():
    base = int(input("Digite um número:\n"))
    potencia = int(input("Digite um outro número:\n"))
    
    valor = base**potencia
    print(f'A potência {base}^{potencia} -> {valor}')


#Exer 2 - Crie um programa que peça ao usuário para inserir um número e calcule a raiz quadrada desse número. Ao fim, mostre o número como um valor monetário do Brasil

def exer_2(): 
    numero = int(input("Digite um número:\n"))
    if numero >= 0:
        raiz = round(math.sqrt(numero), 2)
        print(f"O valor da raiz é R$ {raiz}")
    else:
        print("Não existe raiz negativa")


#Exer 3 - Crie um programa que peça ao usuário para inserir um ângulo em graus e calcule o seno, cosseno e a tangente desse ângulo.

def exer_3():
    angulo = float(input("Digite um ângulo de valor entre 0° e 360°:\n"))
    pi = math.pi
  
    seno = math.sin(angulo*pi/180)
    cos = math.cos(angulo*pi/180)
    tan = math.tan(angulo*pi/180)
    print("Seno do ángulo: " + str(seno))
    print("Cosseno do ángulo: " + str(cos))
    print("Tangente do ángulo: " + str(tan))

#Exer 4 - Crie um programa que peça ao usuário para inserir um número e calcule o logaritmo natural desse número.

def exer_4():
    numero = float(input("Digite um número:\n"))
    ln = math.log(numero)
    math.e
    print(f'O logaritmo natural é {ln}')


#Exer 5 - Crie um programa que peça ao usuário para inserir um número e calcule o fatorial desse número.

def exer_5():
    #Decidi ser preguiçoso e usar as funções da biblioteca math. Fiz fatorial com loop for em outro capítulo
    numero = int(input("Digite um número:\n"))
    print(f'Fatorial do número: {math.factorial(numero)}')



#Exer 6 - Crie um programa que peça ao usuário para inserir dois números complexos e calcule a soma e o produto desses números. 

def exer_6():
    a1 = float(input("Um número complexo pode ser representado como z = a +bi, onde é a raiz de menos 1. Digite a parte real deste número caso ela exista:\n"))
    b1 = float(input("Digite a parte imaginário:\n"))
    z1 = a1 + b1

    a2 = float(input("Um número complexo pode ser representado como z = a +bi, onde é a raiz de menos 1. Digite a parte real deste número caso ela exista:\n"))
    b2 = float(input("Digite a parte imaginário:\n"))
    z2 = a2 + b2

    print(f'Soma é z = {a1 + a2} + {b1 + b2}i')
    print(f'Produto é z = ({a1*a2} - {a1*b2} + ({a1*b2 + b1*a1})i)')
    

#Exer 7 - Crie um programa que peça ao usuário para digitar o nome de usuário e uma senha contendo apenas caracteres alfanuméricos e use uma expressão regular para fazer uma limpeza nos valores digitados, exibindo novamente para o usuário os valores processados. 

def exer_7():
    nome = input("Digite seu nome:\n")
    senha = input("Digite sua senha:\n")

    nome_nov = re.sub(r'\W','',nome)
    senha_nov = re.sub(r'\W','',senha)

    print(nome_nov)
    print(senha_nov)


exer_7()

#Exer 8 - Crie um programa que peça ao usuário para digitar uma frase com 5 palavras. Caso a frase digitada tenha uma quantidade diferente de palavras, o usuário deve digitar novamente. Ao fim, mostre uma palavra por linha. Use expressões regulares para extrair as palavras.

def exer_8():
    saida = True
    while saida:
        frase = input("Digite uma frase com cinco palavras:\n")
        frase_quebrada = re.split("\s",frase)
        if len(frase_quebrada) != 5:
            print("Quantidade de palavras diferente de 5!")
        else:
            for i in frase_quebrada:
                print(i)
            saida = False

#Exer 9 - Crie um programa que peça ao usuário para digitar um CPF e use uma expressão regular para verificar se o CPF está no formato DDD.DDD.DDD-DD, onde D corresponde a um dígito entre 0 e 9.

def exer_9():
    #Este pesquisei na internet.
    cpf = input("Digite seu CPF no formato DDD.DDD.DDD-DD:\n")
    padrao = re.compile(r"^([0-9]{3}[.]?[0-9]{3}[.]?[0-9]{3}[-]?[0-9]{2})$")
    resposta = padrao.search(cpf)
    if resposta:
        print("Válido")
    else:
        print("Inválido")

#Exer 10 - Crie um programa que peça ao usuário para digitar uma frase e que, em seguida, use expressão regular para extrair todos os artigos da frase. Ao fim, o programa deve mostrar a frase sem os artigos.

def exer_10():
    frase = input("Digite uma frase:\n")
    artigos_regex = r'\b(o|a|os|as|um|uma|uns|umas)\b'
    frase_sem_artigos = re.sub(artigos_regex, '', frase, flags=re.IGNORECASE)
    print("Frase sem artigos:", frase_sem_artigos.strip())



#Exer 11 - Crie um programa que peça ao usuário para digitar uma frase e que, em seguida, fatie a frase em substrings de 6 caracteres e mostre-as uma por linha.

def exer_11():
    frase = input("Digite uma frase:\n")
    tamanho = len(frase)
    if tamanho <= 6:
        print(frase)
    else:
        espacos_regex = r'\s+'
        frase_sem_espacos = re.sub(espacos_regex, '', frase)
        inicio = 0
        fim = 6
        for i in range(0,tamanho+1, 6):
            print(i)
            print(frase_sem_espacos[inicio:fim])
            inicio = fim
            fim = i+6
        print("-------")
        print(frase_sem_espacos)            


#Exer 12 - Crie um programa que peça ao usuário para digitar uma frase e que, em seguida, verifique quantas palavras terminam com a letra "o" e quantas terminam com a letra "a".

def exer_12():
    frase = input("Digite uma frase:\n")
    frase_quebrada = re.split("\s",frase)
    quantidadeA = 0
    quantidadeO = 0

    for i in frase_quebrada:
        if i.endswith("o"):
            quantidadeO+=1
        elif i.endswith("a"):
            quantidadeA+=1
    print(f'Quantidade de letras a: {quantidadeA} e quantidade de letras o: {quantidadeO}')

#Exer 13 - Crie um programa que peça ao usuário para digitar uma frase, divida-a em palavras, remova todos os espaços em branco desnecessários dessas palavras, e componha a frase novamente com apenas 1 espaço entre as palavras. 

def exer_13():
    frase = input("Digite uma frase:\n")
    frase_quebrada = re.split("\s",frase)
    print(frase_quebrada)
    frase_nova = ''
    for i in frase_quebrada:
        if i != '':
            frase_nova =  frase_nova + str(i) + " "
    print(frase_nova)
        

#Exer 14 - Crie um programa que peça ao usuário para digitar um frase e que, em seguida, mostre a posição inicial de cada palavra contida nessa frase. 

def exer_14():
    frase = input("Digite uma frase:\n")
    frase_quebrada = re.split("\s",frase)
    for i in frase_quebrada:
        print(frase_quebrada.index(i))

#Exer 15 - Crie um programa que peça ao usuário para digitar uma frase e que, em seguida, mostre quantas vezes cada palavra aparece nessa frase.

def exer_15():
    frase = input("Digite uma frase:\n")
    frase_quebrada = re.split("\s",frase)
    vetor = []
    for i in frase_quebrada:
        contagem = 0
        for k in frase_quebrada:
            if i == k:
                contagem +=1
        if [i, contagem] not in vetor:
            vetor.append([i,contagem])
    
    print(vetor)
#-----------------------------------------------------------
#Chamando a função

exer_15()
