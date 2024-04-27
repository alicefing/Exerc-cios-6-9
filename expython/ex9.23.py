def somar_numeros(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            numeros = [int(numero) for numero in arquivo.readlines()]
            soma = sum(numeros)
            print("Soma dos números:", soma)
    except FileNotFoundError:
        print("Arquivo nãoencontrado")
    except ValueError:
        print("Arquivo com valores inválidos")
    except Exception as e:
        print("Ocorreu um erro", e)

nome_arquivo = "numeros.txt"
somar_numeros(nome_arquivo)