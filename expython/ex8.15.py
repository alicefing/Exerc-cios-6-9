class Produto:
    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque
    
    def mostrar_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Preço: R${self.preco:.2f}")
        print(f"Quantidade em estoque: {self.estoque}")

class ProdutoImportado(Produto):
    def __init__(self, nome, preco, estoque, imposto):
        super().__init__(nome, preco, estoque)
        self.imposto = imposto
    
    def preco_final(self):
        preco_final = self.preco * (1 + self.imposto)
        return preco_final


produto_importado = ProdutoImportado("Iphone", 3500.00, 5, 1.2)
produto_importado.mostrar_dados()
print(f"Preço final com imposto: {produto_importado.preco_final():.2f}")

