def filtrar_elementos(lista, funcao):
    nova_lista = []
    for elemento in lista:
        if funcao(elemento):
            nova_lista.append(elemento)
    return nova_lista

def maior_que_cinco(x):
    return x > 5

lista_original = [1, 7, 3, 9, 2, 6, 4, 8]
nova_lista = filtrar_elementos(lista_original, maior_que_cinco)
print("Lista com elementos maiores que cinco:", nova_lista)