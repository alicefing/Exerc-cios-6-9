import os

nome_diretorio = "temp"
nome_arquivo = "temp.txt"

try:
    os.mkdir(nome_diretorio)
    print(f"O diretório {nome_diretorio} foi criado")
    caminho_arquivo = os.path.join(nome_diretorio, nome_arquivo)

    with open(caminho_arquivo, 'w') as arquivo:
        arquivo.write("Este é o arquivo temp.txt dentro do diretório temp")
        print(f"O arquivo {nome_arquivo} foi criado dentro do diretório {nome_diretorio}")

    os.remove(caminho_arquivo)
    print(f"O arquivo {nome_arquivo} foi excluído")
    os.rmdir(nome_diretorio)
    print(f"O diretório {nome_diretorio} foi excluído")

except FileExistsError:
    print(f"O diretório {nome_diretorio} já existe")
except FileNotFoundError:
    print(f"O diretório {nome_diretorio} não encontrado")