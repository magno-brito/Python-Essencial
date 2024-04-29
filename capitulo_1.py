import math

# 1.1 Crie um programa que armazene seu nome e dua idade em variáveis separadas e imprima uma saída formatada com elas.

def exer_1():
    nome = str(input("Digite seu nome:\n"))
    idade = int(input("Digite sua idade:\n"))
    print('Seu nome é {} e sua idade é {}'.format(nome,idade))

# 1.2 Crie um programa que armazene dois números em variáveis separadas e imprima a soma, subtração, multiplicação e divisão desses números.

def exer_2():
    numero_A = float(input("Digite um número:\n"))
    numero_B = float(input("Digite outro número:\n"))

    print("Soma de A e B:" + str(numero_A + numero_B))
    print("Subtração de A e B:" + str(numero_A - numero_B))
    print("Produto de A e B:" + str(numero_A*numero_B))
    print("Razão de A e B:" + str(numero_A/numero_B))


# 1.3 Crie um programa que peça ao usuário para digitar três números, armazenando-os em variáveis distindas. Em seguida, imprima a média aritmética dos três números. 
    
def exer_3():
    numero1 = float(input("Digite o primeiro número:\n"))
    numero2 = float(input("Digite o segundo número:\n"))
    numero3 = float(input("Digite o terceiro número:\n"))

    print("A média aritmética dos números fornecidos são: " + str((numero1+numero2+numero3)/3))


# 1.4 Crie um programa que peça ao usuário para digitar seu peso e sua altura. Em seguida calcule o índice de massa corporal (IMC) e imprima o resultado. A fórmula do IMC é:
    # IMC = peso/altura²

def exer_4():
    print(2^3)
    peso = float(input("Digite seu peso:\n"))
    altura = float(input("Digite sua altura:\n"))

    imc = peso/(altura**2)

    print("O resultado de seu IMC é: " + str(imc))



#Exer 5: Crie um programa que peça ao usuário para digitar três números e imprima a soma

def exer_5():
    # a = float(input("Digite um número a:\n"))
    # b = float(input("Digite um número b:\n"))
    # c = float(input("Digite um número c:\n"))

    #Vi esta nova forma de fazer múltiplos inputs também. Digite os três números separados com espaço
    a,b,c = input("Digite um número:").split()

    print("A soma de a, b e c é: " + str(float(a)+float(b)+float(c)))


#Exer 6: Crie um programa que peça ao usuário para digitar um número. Em seguida, o programa deve calcular e mostrar a raiz quadrada desse numero

def exer_6():
    #importei a biblioteca math
    numero = float(input("Digite um número que não seja negativo:\n"))
    print("A raiz quadrada deste número é: " + str(math.sqrt(numero)))

#Exer 7: Crie um programa que peça ao usuário para digitar um número inteiro. Em seguida, o programa deve calcular e mostrar o valor dos inteiros anterior e posterior a esse número

def exer_7():
    numero = int(input("Digite um número que inteiro:\n"))
    posterior = numero + 1
    anterior = numero -1
    print("Anterior do número: " + str(anterior))
    print("Posterior do número: " + str(posterior))

#Exer 8: Crie um programa que peça ao usuário para digitar um ângulo entre 0 e 360 graus. Em seguida, o programa deve calcular e mostrar o seno, cosseno e a tangente desse número.

def exer_8():
    angulo = float(input("Digite um ângulo de valor entre 0° e 360°:\n"))
    pi = math.pi
  
    seno = math.sin(angulo*pi/180)
    cos = math.cos(angulo*pi/180)
    tan = math.tan(angulo*pi/180)
    print("Seno do ángulo: " + str(seno))
    print("Cosseno do ángulo: " + str(cos))
    print("Tangente do ángulo: " + str(tan))

    #Alguns valores são bem aproximados e não utilizei a função round para não ter diferença. Por exemplo, cosseno de 90 é 0 mas ele da como resultado um número com potência de -17 que é um valor bem próximo de zero. 



#Exer 9: Crie um programa que peça ao usuário para digitar dois números quaisquer. Em seguida, o programa deve calcular e mostrar a potência do primeiro número pelo segundo. 

def exer_9():
    b,p = input("Digite dois números inteiros: ").split()
    potência = int(b)**int(p)
    print("Potência de b por p é: " + str(potência))

#Exer 10: Crie um programa que peça ao usuário para digitar três números (A,B e C). Em seguida o programa deve calcular e mostrar os valores das raízes da seguinte equação, usando a fórmula de Bhaskará Ax² + Bx + C = 0

def exer_10():
    A = float(input("Digite um número A: \n"))
    B = float(input("Digite um número B: \n"))
    C = float(input("Digite um número C: \n"))

    try:
        delta = math.sqrt(B**2 - 4*A*C)
        print(delta)
        raiz_A = (-B + delta)/(2*A)
        print(A)
        raiz_B = (-B - delta)/(2*A)
        print("As raízes são " + str(raiz_A) + " e " + str(raiz_B))
    except:
        print("Não existe raízes possíveis")
    
    


#Exer 11: Crie um programa que peça ao usuário para digitar o raio de um círculo. Em seguida, o programa deve calcular e mostrar a área e o comprimento do círculo.

def exer_11():
    raio = float(input("Digite o raio de um círculo: \n"))
    if raio < 0: raio*=(-1)
    area = round(math.pi*raio**2,2)
    comprimento = round(math.pi*2*raio,2)

    print("Área: " + str(area))
    print("Comprimento: " + str(comprimento))

#Exer 12: Crie um programa que peça ao usuário para digitar as dimensões de um retângulo (largura e altura). Em seguida, o programa deve calcular e mostrar a área e o perímetro desse retângulo.

def exer_12():
    comprimento = float(input("Digite o comprimento de um retângulo: \n"))
    altura = float(input("Digite a altura de um retângulo: \n"))
    if comprimento < 0: comprimento*=-1
    if altura < 0: altura*=-1
    area = comprimento*altura
    perimetro = 2*comprimento + 2*altura
    print("Área do retângulo: " + str(area))
    print("Perímetro do retângulo: " + str(perimetro))

#Exer 13: Crie um programa que peça ao usuário para digitar a base e a altura de um triângulo. Em seguida, o programa deve calcular e mostrar a área desse triângulo.

def exer_13():
    base = float(input("Digite a base do triângulo: \n"))
    altura = float(input("Digite a altura do triângulo: \n"))
    if base < 0: base *=-1
    if altura < 0: altura*=-1
    area = base*altura/2

    print("Área do triângulo é: " + str(area))

#Exer 14: Crie um programa que peça ao usuário para digitar o nome, preço de custo, o preço de venda e a quantidade em estoque de um determinado produto. Em seguida, o programa deve calcular e mostrar o lucro que esse produto pode gerar se todo o estoque for vendido.

def exer_14():
    nome = input("Digite o nome do produto:\n")
    preco_custo = float(input("Digite o preço de custo:\n"))
    preco_venda = float(input("Digite o preço de venda:\n"))
    quantidade_em_estoque = int(input("Digite a quantidade em estoque do produto:\n"))

    lucro = quantidade_em_estoque*(preco_venda-preco_custo)
    print(f"O lucro obtido {nome} se todo o estoque for vendido é de R$ {lucro}")

#Exer 15: Crie um programa que peça ao usuário para digitar o valor total de uma venda, o percentual de desconto aplicado e o percentual de imposto cobrado. Ao fim, o programa deve mostrar o preço final da mercadoria, sendo que o imposto é cobrado sobre o valor com desconto.

def exer_15():
    valor_total = float(input("Digite o valor total da venda:\n"))
    desconto = float(input("Digite o percentual de desconto (%): \n"))
    imposto = float(input("Digite o percentual do imposto cobrado(%):\n"))

    preco_sem_imposto = valor_total - valor_total*(desconto/100)
    preco_final = preco_sem_imposto - preco_sem_imposto*(imposto/100)
    print(f"O valor final é R$ {preco_final}")


#---------------------------------------------------------------

#Chame aqui cada função para executar os exercícios

exer_1()
