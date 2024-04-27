class ContaBancaria:
    def __init__(self, saldo=0):
        self.saldo = saldo
    
    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito de R${valor:.2f} realizado")
    
    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado")
        else:
            print("Saldo insuficiente")
    
    def consultar_saldo(self):
        print(f"Saldo disponível: R${self.saldo:.2f}")

class ContaPoupanca(ContaBancaria):
    def __init__(self, saldo=0, taxa_juros=0.01):
        super().__init__(saldo)
        self.taxa_juros = taxa_juros
    
    def rendimento(self):
        rendimento_mensal = self.saldo * self.taxa_juros
        print(f"O rendimento mensal é de R${rendimento_mensal:.2f}")


conta_poupanca = ContaPoupanca()
conta_poupanca.depositar(4000)
conta_poupanca.taxa_juros = 0.005
conta_poupanca.rendimento()