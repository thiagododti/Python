"""
    Método de classe + factories (fábricas)
    São métodos onde "self" será "cls", ou seja
    ao invés de receber a instância no primeiro
    parâmetro, receberemos a própria class.
"""


class Pessoa:
    ano = 2023

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def criar_anonimo(cls, idade):
        return cls("Anônimo", idade)

# Criando uma nova inst


p1 = Pessoa.criar_anonimo(20)

print(p1.nome, p1.idade)  # Anônimo 20
