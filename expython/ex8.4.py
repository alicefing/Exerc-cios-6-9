class Carro:
    def __init__(self):
        self.velocidade = 0
    
    def acelerar(self, tempo):
        aceleracao = 10  
        self.velocidade += aceleracao * tempo
        print(f"O carro acelerou {self.velocidade} m/s")
    
    def frear(self, tempo):
        desaceleracao = 5  
        self.velocidade -= desaceleracao * tempo
        if self.velocidade < 0:
            self.velocidade = 0
        print(f"O carro freou {self.velocidade} m/s")


carro = Carro()
carro.acelerar(10)  
carro.frear(6)  