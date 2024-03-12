import json

CAMINHO_ARQUIVO = 'POO/classes/ex-salvajson/class.json'


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


p1 = Pessoa('Thiago', 31)
p2 = Pessoa('Mariana', 25)
p3 = Pessoa('Lucas', 28)

bd = [vars(p1), p2.__dict__, vars(p3)]

with open(CAMINHO_ARQUIVO, 'w') as arquivo:
    json.dump(bd, arquivo, ensure_ascii=False, indent=2)
