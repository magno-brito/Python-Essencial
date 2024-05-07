# Exer 6 -> Crie uma classe chamada Circulo com um método __init__ que inicialize o raio do círculo. Crie um método chamado area que retorne a área do círculo. Crie uma instância da classe Circulo e chame o metodo area.
import math

class Circulo:
    def __init__(self, raio):
        self.raio = raio
    
    def area(self):
        return round(math.pi*self.raio**2,2)
    

cirulo = Circulo(2)
print(cirulo.area())