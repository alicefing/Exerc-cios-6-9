class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
    
    def perimetro(self):
        return self.lado1 + self.lado2 + self.lado3

class TrianguloRetangulo(Triangulo):
    def __init__(self, lado1, lado2, lado3):
        super().__init__(lado1, lado2, lado3)
    
    def area(self):
        hipotenusa = max(self.lado1, self.lado2, self.lado3)
        cateto1, cateto2 = sorted([self.lado1, self.lado2, self.lado3])[:2]
        area = (cateto1 * cateto2) / 2
        return area

triangulo_retangulo = TrianguloRetangulo(3, 4, 5)
print(f"{triangulo_retangulo.perimetro()} é o perímetro do triângulo retângulo")
print(f"{triangulo_retangulo.area()} é a área do triângulo retângulo")