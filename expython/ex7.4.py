import os

nome_arquivo = input("Digite o nome do arquivo: ")

if os.path.isfile(nome_arquivo):
    novo_nome = nome_arquivo + "_renomeado" + os.path.splitext(nome_arquivo)[1]
    
    try:
        os.rename(nome_arquivo, novo_nome)
        print(f"O arquivo foi renomeado para {novo_nome}")
    except OSError:
        print("Erro ao renomear o arquivo")
else:
    print("O arquivo não existe")