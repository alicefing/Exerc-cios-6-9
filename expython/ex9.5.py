# Da seguinte forma, exemplo:

try:
    arquivo = open("arquivo.txt", "r")
    conteudo = arquivo.read()
    arquivo.close()
except Exception as e:
    print("Ocorreu um erro:", e)