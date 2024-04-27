class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def mostrar_dados(self):
        print(f"Nome: {self.nome} | Idade: {self.idade}")

class Funcionario(Pessoa):
    def __init__(self, nome, idade, salario):
        super().__init__(nome, idade)
        self.salario = salario
    
    def aumentar_salario(self, aumento):
        self.salario += self.salario * (aumento / 100)

    def mostrar_dados(self):
        super().mostrar_dados()
        print(f"Salário: R${self.salario:.2f}")    

funcionario = Funcionario("Alice", 19, 5000)
funcionario.aumentar_salario(100)
funcionario.mostrar_dados()