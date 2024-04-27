class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def mostrar_dados(self):
        print(f"Nome: {self.nome}, Idade: {self.idade}")

class Funcionario(Pessoa):
    def __init__(self, nome, idade, salario):
        super().__init__(nome, idade)
        self.salario = salario
    
    def mostrar_dados(self):
        super().mostrar_dados()
        print(f"Salário: R${self.salario:.2f}")

pessoas_e_funcionarios = [
    Pessoa("Alice", 19),
    Pessoa("Anna", 22),
    Funcionario("Elis", 35, 3400),
    Funcionario("Pedro", 32, 1200)
]

for pessoa_ou_funcionario in pessoas_e_funcionarios:
    pessoa_ou_funcionario.mostrar_dados()