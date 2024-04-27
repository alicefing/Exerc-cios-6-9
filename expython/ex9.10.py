#Da seguinte maneira: 
#Deve-se criar uma nova classe que herda 
#uma das classes base de exceção

class Excecao(Exception):
    def __init__(self, mensagem):
        self.mensagem = mensagem

    def __str__(self):
        return f'{self.mensagem}'

try:
    raise Excecao("Houve algum erro")
except Excecao as e:
    print(e)