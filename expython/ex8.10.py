class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def mostrar_dados(self):
        print(f"Nome: {self.nome} | Idade: {self.idade}")

class Cliente(Pessoa):
    def __init__(self, nome, idade, endereco):
        super().__init__(nome, idade)
        self.endereco = endereco
    
    def mostrar_dados(self):
        super().mostrar_dados()
        print(f"Endereço: {self.endereco}")


cliente1 = Cliente("Alice", 19, "Rua José Basílio, Alto Monte Cristo")
cliente1.mostrar_dados()