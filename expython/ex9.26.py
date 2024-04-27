from funcao import dividir_numeros

def main():
    try:
        resultado = dividir_numeros(10, 2)  
        print("Resultado da divisão:", resultado)
    except ZeroDivisionError:
        print("Erro: Divisão por zero")
    except Exception as e:
        print("Erro:", e)

if __name__ == "__main__":
    main()