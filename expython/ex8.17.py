import math

class Circulo:
    def __init__(self, raio):
        self.raio = raio
    
    def area(self):
        return math.pi * self.raio**2

class Cilindro(Circulo):
    def __init__(self, raio, altura):
        super().__init__(raio)
        self.altura = altura
    
    def volume(self):
        return self.area() * self.altura


cilindro = Cilindro(raio=5, altura=10)
print(f"{cilindro.area()} é a área da base do cilindro")
print(f"{cilindro.volume()} é o volume do cilindro")