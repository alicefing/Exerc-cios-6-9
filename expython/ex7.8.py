import shutil

nome_diretorio = "temp"

try:
    shutil.rmtree(nome_diretorio)
    print(f"O diretório {nome_diretorio} foi excluído")
except FileNotFoundError:
    print(f"O diretório {nome_diretorio} não encontrado")