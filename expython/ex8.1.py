class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def mostrar_dados(self):
        print(f"Nome: {self.nome}, Idade: {self.idade}")

pessoa1 = Pessoa("Alice", 19)
pessoa2 = Pessoa("Anna", 22)

pessoa1.mostrar_dados()
pessoa2.mostrar_dados()