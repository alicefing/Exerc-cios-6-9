def composicao(funcao1, funcao2):
    def funcao_composta(arg):
        return funcao1(funcao2(arg))
    return funcao_composta

def dobro(x):
    return x * 2

def soma(x):
    return x + 1

resultado = composicao(dobro, soma)(3)
print(f"Resultado de dobrar e incrementar é {resultado}")