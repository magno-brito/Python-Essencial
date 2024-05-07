    
#Exer 7 -> Crie uma classe chamada Pessoa com um método __init__ que inicialize o nome e a idade da pessoa, e um método mostrar_dados que exiba o nome e a idade da pessoa. Crie uma classe chamada Funcionario que herde da classe Pessoa e adicione um atributo salario e um método chamado mostrar_dados que exiba o nome, a idade e o salário do funcionário. Crie uma lista com duas pessoas e dois funcionários e faça um laço para chamar o método mostrar_dados de todos os objetos dessa lista.

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def mostrar_dados(self):
        print(F"Nome: {self.nome} e Idade: {self.idade}")

class Funcionario(Pessoa):
    def __init__(self,nome, idade, salario):
        super().__init__(nome, idade)
        self.salario = salario

    def mostrar_dados(self):
        print(F"Nome: {self.nome}, Idade: {self.idade} e Salario:{self.salario}")

lista = list()
pessoaA = Pessoa("Juca", 40)
lista.append(pessoaA)
pessoaB = Pessoa("Josefina", 30)
lista.append(pessoaB)
funcionarioA = Funcionario("Marcos", 32, 1000)
lista.append(funcionarioA)
funcionarioB = Funcionario("Maria", 64, 2000)
lista.append(funcionarioB)

for gente in lista:
     gente.mostrar_dados()