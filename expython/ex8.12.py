class Veiculo:
    def __init__(self):
        self.velocidade = 0
    
    def acelerar(self, valor):
        self.velocidade += valor
    
    def frear(self, valor):
        self.velocidade -= valor
    
    def exibir_velocidade(self):
        print(f"A velocidade do {self.marca} é: {self.velocidade} km/h")

class Carro(Veiculo):
    def __init__(self, marca):
        super().__init__()
        self.marca = marca


carro1 = Carro("Fusca")
carro1.acelerar(100)
carro1.exibir_velocidade()
carro1.frear(20)
carro1.exibir_velocidade()