class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
    
    def area(self):
        return self.largura * self.altura

retangulo = Retangulo(6, 3)
print(f"{retangulo.area()} é a área do triaângulo")