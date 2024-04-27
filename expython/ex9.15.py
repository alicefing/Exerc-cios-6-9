#Exemplo:

try:
    raise ValueError("Erro original")
except ValueError as e:
    raise TypeError("Novo erro") from e