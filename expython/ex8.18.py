class Animal:
    def __init__(self, nome):
        self.nome = nome
    
    def emitir_som(self):
        return "O animal emite um som genérico."

class Cachorro(Animal):
    def emitir_som(self):
        return "au au!"


cachorro = Cachorro("Luli")
som_emitido = cachorro.emitir_som()
print(f"{cachorro.nome} faz {som_emitido}")