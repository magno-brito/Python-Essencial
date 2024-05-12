#Exer 6 -> Implemente um jogo de adivinhação em que o usuário deve acertar um número entre 1 e 10. Utilize o tratamento de exceções para garantir que o usuário insira apenas números válidos.
import random

while True:
    numero = random.randrange(10)
    palpite = int(input("Digite um número inteiro entre 1 e 10 ou 0 para sair:\n"))
    
    if numero == palpite:
        print("Você acertou")
    else:
        print("Errou")
    if palpite < 0 or palpite > 10:
        raise ValueError("Valor fora do intervalo")
    if palpite == 0:
        print("Saiu")
        break
    
    
    
        