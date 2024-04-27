lista1 = [1, 2, 3, 4, 5]
lista2 = [4, 5, 6, 7, 8]


intersecao = lambda lista1, lista2: [x for x in lista1 if x in lista2]
resultado = intersecao(lista1, lista2)
print("Elementos em comum entre as listas:", resultado)