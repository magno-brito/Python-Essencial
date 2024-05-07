# Exer 4 -> Crie uma classe chamada ContaBancaria com os métodos depositar e sacar. Utilize tratamento de exceções para lidar com saques maiores que o saldo disponível, criando uma exceção personalizada.


class Conta_Bancaria:

    def __init__(self, saldo):
        self.saldo = saldo

    def depositar(self, valor):
        if valor < 0:
            raise ValueError("Não é possível depósitos negativos")
        self.saldo += valor
    
    def sacar(self, valor):
        if valor > self.saldo:
            raise ValueError("Não é possível sacar um valor maior que o saldo")
        self.saldo -= valor
    
    def exibir_saldo(self):
        print(f"Saldo R$ {self.saldo}")

conta = Conta_Bancaria(100)
conta.depositar(-1)
conta.sacar(200)