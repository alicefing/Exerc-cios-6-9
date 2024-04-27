def fatorial(f):
    if f == 0:
        return 1
    else:
        return f * fatorial(f - 1)

numero = 5
resultado = fatorial(numero)
print(f'O fatorial de {numero} é {resultado}')