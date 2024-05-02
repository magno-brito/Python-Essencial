#Exer 4 - Crie uma classe chamada Carro com o atributo velocidade e com métodos para acelerar e frear o carro com X segundos, sendo o carro acelera com 10 m/s² e freia a 5 m/s². Crie uma instância da classe Carro e teste os métodos criados.

class Carro:
    
    def __init__(self, velocidade):
        self.velocidade = velocidade
    
    def acelerar(self, tempo: float) -> None:
        self.velocidade = self.velocidade + 10*tempo
    
    def frear(self, tempo: float) -> None:
        self.velocidade = self.velocidade - 5*tempo

    def mostrar_velocidade(self):
        return self.velocidade