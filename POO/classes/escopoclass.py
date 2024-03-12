# Uma variável definida dentro de um método
# nao pode ser acessada dentro de outro método sem que
# seja referenciado ele mesmo através do self.

class Animal:
    def __init__(self, nome):
        self.nome = nome

        variavel = 'valor'
        print(variavel)

    def comendo(self, alimento):
        return f'{self.nome} está comendo {alimento}'

    def acao(self):
        print(variavel)


leao = Animal('Leão')
print(leao.nome)
8
# vai dar erro pois a variável esta definida no escopo do __init__
print(leao.acao())