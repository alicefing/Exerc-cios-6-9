nome = input("Digite o nome do arquivo: ")

try:
    with open(nome, 'r') as arquivo:
        numero_linhas = len(arquivo.readlines())
        print(f'{numero_linhas} é a quantidade de linhas que o arquivo possui.')
except FileNotFoundError:
    print("O arquivo não encontrado")