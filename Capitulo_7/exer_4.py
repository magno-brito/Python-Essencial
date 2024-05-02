#Exer 4 - Crie um programa que solicite ao usuário o nome de um arquivo e que renomeie esse arquivo adicionando a palavras "renomeado" ao nome existente, mantendo sua extensão.

import os

original = input("Digite o nome do arquivo (com extensão): ")
nome, extensao = os.path.splitext(original)
renomeado = f"{nome}_renomeado{extensao}"


if os.path.exists(original):
    os.rename(original, renomeado)
    print(f"Arquivo renomeado para: {renomeado}")
else:
    print(f"Arquivo '{original}' não encontrado.")
