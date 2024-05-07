#Exer 9 -> Crie uma classe chamada Retângulo com um método __init__ que inicialize a largura e a altura do retângulo. Crie um método chamado area que retorne a área do retângulo. Crie uma classe chamada Quadrado que herde da classe Retangulo e substitua o método __init__ para que seja necessario apenas informar um lado, ao invés de largura e altura. Crie uma instância da classe Quadrado e chame o método área. 

class Retangulo:
    def __init__(self, largura, altura):
        self.altura = altura
        self.largura = largura

    def area(self):
        return self.largura*self.altura
    

class Quadrado(Retangulo):
    def __init__(self, lado):
        super().__init__(lado, lado)
    

quadrado = Quadrado(5)
print(quadrado.area())