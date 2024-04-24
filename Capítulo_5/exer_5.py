#Exer 5 : Crie uma função que defina uma variável x dentro da função e imprima o valor de x na tela. Em seguida, fora da função, crie uma linha de comando para imprimir o valor de x e analise o erro que será gerado ao tentar executar o programa. 

def exer_5(x=3):
    print(x)

print(exer_5())

#O erro é que a função retorna None então nada será impresso!
