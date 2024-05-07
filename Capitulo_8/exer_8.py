#Exer 8 -> Crie uma classe chamada Pessoa com um método __init__ que inicialize o nome e a idade da pessoa, e um método chamado mostrar_dados que exiba o nome e a idade da pessoa. Crie uma classe chamada Aluno que herde da classe Pessoa e adicione um atributo matricula e um método mostrar_dados que exiba o nome, a idade e a matricula do aluno. Crie uma instância da classe Aluno e chame o método mostrar_dados.

class Aluno(Pessoa):
    def __init__(self, nome, idade, matricula):
        super().__init__(nome,idade)
        self.matricula = matricula

    def mostrar_dados(self):
        print(F"Nome: {self.nome}, Idade: {self.idade} e Matricula:{self.matricula}")

aluno = Aluno("Pedro", 16, "20211si009")
aluno.mostrar_dados()