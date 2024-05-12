#Exer 7 -> Crie uma classe Triangulo com os atributos lado1, lado2, e lado3. Implemente um método tipo_triangulo que informe se o triângulo é equilátero, isósceles ou escaleno. Utilize o tratamento de exceções para lidar com triângulos inválidos.

class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
        
        if self.lado1 + self.lado2 <= self.lado3 or self.lado2 + self.lado3 <= self.lado1 or self.lado1 + self.lado3 <= self.lado2:
            raise ValueError("Valores não formam um triângulo")
        
    def tipo_de_triangulo(self):
        if self.lado1 == self.lado2 and self.lado1 != self.lado3 or self.lado1 == self.lado3 and self.lado1 != self.lado2 or self.lado3 == self.lado2 and self.lado1 != self.lado3 :
            print("Triângulo isosceles")
            
        if self.lado2 != self.lado1 and self.lado3 != self.lado2 and self.lado3 != self.lado1:
            print("Triângulo escaleno")
        
        if self.lado2 == self.lado1 and self.lado2 == self.lado3:
            print("Triângulo equilátero")

triangulo = Triangulo(15,20,5)
triangulo.tipo_de_triangulo()