#Exer 1 - Crie uma classe chamada Pessoa com um método __init__ que inicialize o nome e a idade da pessoa. Crie um método chamado mostrar_dados que exiba o nome e a idade da pessoa. Crie duas instâncias da classe Pessoa e chame o método mostrar_dados de cada uma das instâncias. 

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def mostrar_dados(self):
        print(f"Nome {self.nome} e idade {self.idade} anos")