#Exer 2 -> Crie uma função que receba uma lista de números e retorne a média aritmétrica deles. Trate exceções caso a lista seja vazia ou contenha valores não numéricos.

def exer_2(lista: list) -> float:
    soma = 0
    try:
        for item in lista:
            soma += item
        return soma/(len(lista))
    except ZeroDivisionError:
        print("A lista vazia")
    except:
        print("Lista contém letras")
        

listaA = [2,3,4,5]
listaB = []
listaC = [1,'a']

print(exer_2(listaA))
exer_2(listaB)
exer_2(listaC)

    
