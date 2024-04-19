import math

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
    print("Ok")

#Exer 11: Crie um programa que peça ao usuário para digitar o raio de um círculo. Em seguida, o programa deve calcular e mostrar a área e o comprimento do círculo.

def exer_11():
    print("Ok")

#Exer 12: Crie um programa que peça ao usuário para digitar as dimensões de um retângulo (largura e altura). Em seguida, o programa deve calcular e mostrar a área e o perímetro desse retângulo.

def exer_12():
    print("Ok")

#Exer 13: Crie um programa que peça ao usuário para digitar a base e a altura de um triângulo. Em seguida, o programa deve calcular e mostrar a área desse triângulo.

def exer_13():
    print("Ok")

#Exer 14: Crie um programa que peça ao usuário para digitar o nome, preço de custo, o preço de venda e a quantidade em estoque de um determinado produto. Em seguida, o programa deve calcular e mostrar o lucro que esse produto pode gerar se todo o estoque for vendido.

def exer_14():
    print("Ok")

#Exer 15: Crie um programa que peça ao usuário para digitar o valor total de uma venda, o percentual de desconto aplicado e o percentual de imposto cobrado. Ao fim, o programa deve mostrar o preço final da mercadoria, sendo que o imposto é cobrado sobre o valor com desconto.

def exer_15():
    print("Ok")

#---------------------------------------------------------------

exer_9()