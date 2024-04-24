#Exer 2 : Crie uma função que tenha um número inteiro como parâmetro e retorne True se o número for par e False se o número for ímpar. Em seguida, crie uma chamada para essa função passando argumentos para os parâmetros e mostrando o resultado na tela. 

def exer_2( numero: int) -> bool:
    if numero%2 == 0:
        return True
    return False

verificar1 = exer_2(1)
verificar2 = exer_2(2)

print(f'Teste 1: {verificar1}')
print(f'Teste 2: {verificar2}')