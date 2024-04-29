#Exer 6 : Crie um programa que declare uma lista chamade idades com 5 números inteiros. Logo em seguida, crie uma função chamada adicionar que receba uma lista como parâmetro e que adicione um novo elemento qualquer a essa lista. Feito isso, chame a função adicionar passando a lista idades como argumento. Por fim, após a chamada da função, mostre a lista idades para verificar se o elemento foi adicionado corretamente. 

idades = [x for x in range(1,6)]

def adicionar(lista: list, elemento: int) -> None:
    lista.append(elemento)

adicionar(idades,6)
print(idades)