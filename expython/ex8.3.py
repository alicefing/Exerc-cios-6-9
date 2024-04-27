class ContaBancaria:
    def __init__(self):
        self.saldo = 0
    
    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito de {valor} realizado")
    
    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de {valor} realizado")
        else:
            print("Saldo insuficiente")
    
    def exibir_saldo(self):
        print(f"Saldo atual: {self.saldo}")


conta = ContaBancaria()
conta.exibir_saldo()  
conta.depositar(250)  
conta.exibir_saldo()  
conta.sacar(40)       
conta.exibir_saldo()  
conta.sacar(100)  