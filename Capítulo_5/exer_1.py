#Exer 1: Crie uma função com dois parâmetros numéricos, que retorna a soma dos dois números. Em seguida, crie uma chamada para essa função passando argumentos para os parâmetros e mostrando o resultado na tela.

def exer_1(numeroA: float, numeroB: float) -> float :
    return numeroA + numeroB

soma = exer_1(1,2)
print(f"Soma: {soma}")