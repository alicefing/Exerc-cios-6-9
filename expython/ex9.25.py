class ErroEspecifico(Exception):
    pass

def Erro():
    raise ValueError("Ocorreu um erro específico")

def main():
    try:
        Erro()
    except ErroEspecifico as e:
        print("Erro específico:", e)
    except Exception as e:
        print("Erro genérico:", e)

if __name__ == "__main__":
    main()
