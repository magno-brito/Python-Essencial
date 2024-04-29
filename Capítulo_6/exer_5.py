#Exer 5 - Faça um programa que crie um dicionário com nomes e notas de alunos, ambos digitados pelo usuário, usando os nomes dos alunos como chave e as notas como valor. Em seguida, use dict comprehension para criar um dicionário com os alunos com a nota igual ou superior a 7.

def exer_5()-> dict:
    dicionario = dict()
    while True:
        nome = input("Digite o nome do aluno:\n")
        nota = float(input("Digite a nota ou -1 para sair:\n"))
        if nota == -1.0:
            break
        else:
            dicionario[nome] = nota
    print(dicionario)
    novo_dicio = {chave:valor for (chave, valor) in dicionario.items() if valor >= 7 }
    print(novo_dicio)

exer_5()

