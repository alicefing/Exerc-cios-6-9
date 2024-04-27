def sequencia_fibonacci(f):
    if f <= 1:
        return f
    else:
        return sequencia_fibonacci(f - 1) + sequencia_fibonacci(f - 2)

f = 10
resultado = sequencia_fibonacci(f)
print(f'O {f}-ésimo termo da sequência de Fibonacci é {resultado}')