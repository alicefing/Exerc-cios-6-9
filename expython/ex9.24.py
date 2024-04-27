def mostrar_conteudo():
    while True:
        nome_arquivo = input("Digite o nome do arquivo: ")
        try:
            with open(nome_arquivo, 'r') as arquivo:
                conteudo = arquivo.read()
                print("Conteúdo:")
                print(conteudo)
            break  
        except FileNotFoundError:
            print("Arquivo não encontrado")
        except Exception as e:
            print("Ocorreu um erro ao abrir o arquivo:", e)

mostrar_conteudo()