nome = input("Digite o nome do arquivo: ")

try:
    with open(nome, 'r') as arquivo:
        conteudo = arquivo.read()
        print("Conteúdo do arquivo:")
        print(conteudo)
except FileNotFoundError:
    print("O arquivo não encontrado")