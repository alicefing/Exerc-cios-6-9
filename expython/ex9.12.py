class Erro(Exception):
    def __init__(self, mensagem):
        self.mensagem = mensagem

    def __str__(self):
        return f'Ocorreu um erro: {self.mensagem}'

raise Erro("Este é um erro específico do meu programa.")