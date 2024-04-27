nome_origem = input("Digite o nome do arquivo de origem: ")
nome_destino = input("Digite o nome do arquivo de destino: ")

try:
    with open(nome_origem, 'r') as arquivo_origem, open(nome_destino, 'w') as arquivo_destino:
        for linha in arquivo_origem:
            linha_invertida = linha.strip()[::-1]
            arquivo_destino.write(linha_invertida + '\n')

    print(f"O conteúdo do arquivo {nome_origem} foi invertido e salvo em {nome_destino}.")
except FileNotFoundError:
    print("O arquivo de origem não foi encontrado")