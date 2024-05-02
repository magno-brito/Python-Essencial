#Exer 5 - Crie um arquivo vazio qualquer. Agora, na mesma pasta, crie um programa que solicite ao usuário que digite o nome desse arquivo e exclua-o. 

import os

arquivo = input("Digite o nome do arquivo para excluir (com extensão): ")

if os.path.exists(arquivo):
    os.remove(arquivo)
    print(f"O arquivo '{arquivo}' foi excluído com sucesso.")
else:
    print(f"O arquivo '{arquivo}' não foi encontrado.")
