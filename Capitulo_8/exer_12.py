#Exer 12 -> Crie uma classe chamada Veiculo com os métodos para acelerar, frear e exibir a velocidade do veículo. Crie uma classe chamada Carro que herde da classe Veiculo e adicione um atributo chamado marca. Crie uma instância da classe Carro e teste os métodos criados. 
        
class Veiculo:
    def __init__(self, velocidade):
        self.velocidade = velocidade
    
    def acelerar(self, valor):
        self.velocidade += valor
    
    def frear(self, valor):
        self.velocidade -= valor
    
    def exibir_velocidade(self):
        print(f"Velocidade igual a:{self.velocidade} km/h")

class Carro(Veiculo):
    def __init__(self, velocidade, marca):
        super().__init__(velocidade)
        self.marca = marca
    
    def mostrar_marca(self):
        print(f"Marca: {self.marca}")

carro = Carro(100, "Fiat")
carro.exibir_velocidade()
carro.mostrar_marca()

carro.acelerar(10)
carro.exibir_velocidade()
carro.frear(50)
carro.exibir_velocidade()