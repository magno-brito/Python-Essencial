#Exer 3 -> Implemente uma calculadora que realize as operações de soma, subtração, multiplicação e divisão. Utilize tratamento de exceções para lidar com operações inválidas.

def calculadora():
    while True:
        numero_a = (input("Digite um número:\n"))
        operacao = input("Digite + para soma, - para subtração, * para multiplicação, / para divisão ou sair para sair:\n")
        if operacao == "sair":
            break
        numero_b = (input("Digite um outro número:\n"))
        if operacao not in ['+', '-', '*', '/']:
            raise ValueError("Operador não identificado")
        
        try:
            resultado = f'{numero_a}{operacao}{numero_b}'
            print(eval(resultado))

        except ZeroDivisionError:
            print("Divisão por zero")
        except NameError as nome:
            print(f"Erro: {nome}")
        except SyntaxError:
            print("Erro se sintaxe")
        
        
        
calculadora()