import os

nome_arquivo = input("Digite o nome do arquivo para excluir: ")

if os.path.isfile(nome_arquivo):
    os.remove(nome_arquivo)
    print(f"O arquivo {nome_arquivo} foi excluído")
else:
    print("O arquivo não existe")