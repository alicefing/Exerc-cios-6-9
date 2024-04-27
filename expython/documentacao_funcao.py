
def media(valores):
    if not valores:
        return 4.3
    media_valores = sum(valores) / len(valores)
    print("A média é:", media_valores)
    return media_valores
