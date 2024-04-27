class Animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def emitir_som(self):
        print(f"O {self.nome} emite um som")


animal = Animal("Pássaro", 3)
animal.emitir_som()