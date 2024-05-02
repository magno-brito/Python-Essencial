#Exer 5 - Crie uma classe chamada Animal com um método __init__ que inicialize o nome e a idade do animal. Crie um método chamado emitir_som que exiba um som genérico do animal. Crie uma instância da classe Animal e chame o método emitir_som

class Animal:

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def emitir_som(self):
        return "Cococococococococo"