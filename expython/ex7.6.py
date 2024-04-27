import os
import shutil

nome_arquivo_origem = input("Digite o nome do arquivo original: ")

if os.path.isfile(nome_arquivo_origem):
    nome_arquivo_destino = nome_arquivo_origem + ".copy"
    
    try:
        shutil.copyfile(nome_arquivo_origem, nome_arquivo_destino)
        print(f"O arquivo foi copiado para {nome_arquivo_destino}.")
        with open(nome_arquivo_destino, 'r') as arquivo_copiado:
            print("Conteúdo do arquivo copiado:")
            print(arquivo_copiado.read())
    except OSError:
        print("Erro ao copiar o arquivo.")
else:
    print("O arquivo original não existe.")