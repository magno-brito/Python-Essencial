#Exer 3 - Crie uma classe chamada Conta_Bancaria com o atributo saldo e com métodos depositar, sacar e exibir o saldo da conta. Crie uma instância da classe Conta_Bancaria e teste os métodos criados.

class Conta_Bancaria:

    def __init__(self, saldo):
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
    
    def sacar(self, valor):
        self.saldo -= valor
    
    def exibir_saldo(self):
        print(f"Saldo R$ {self.saldo}")