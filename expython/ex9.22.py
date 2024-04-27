def calcular_media(lista):
    if not lista:
        raise ValueError("A lista está vazia")
    
    soma = sum(lista)
    media = soma / len(lista)
    return media
try:
    lista_vazia = []
    media = calcular_media(lista_vazia)
    print("Média:", media)
except ValueError as ve:
    print(ve)