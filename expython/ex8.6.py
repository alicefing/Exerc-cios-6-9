import math

class Circulo:
    def __init__(self, raio):
        self.raio = raio
    
    def area(self):
        return math.pi * self.raio ** 2

circulo = Circulo(5)
print(f"{circulo.area()} é a área do circulo")