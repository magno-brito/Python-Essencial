#Exer 8 -> Implemente um jogo de adivinhação em que o usuário deve acertar uma palavra secreta. Utilize tratamento de exceções para garantir que o usuário insira apenas letras do alfabeto.

import re

while True:
    palavra = "casa"
    tentativa = input("Digite um palavra (deve conter apenas letras do alfabeta):\n")
    tentativa = tentativa.lower()
    
    if  not re.match('^[a-zA-Z]+$', tentativa):
        raise ValueError("Insira apenas palavras com letras do alfabeto!")
    
    if palavra == tentativa:
        print("Você acertou!")
        break
    else:
        print("Você error. Tente novamente.")