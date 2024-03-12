from app1 import CAMINHO_ARQUIVO, Pessoa
import json

with open(CAMINHO_ARQUIVO, 'r') as arquivo:
    pessoas = json.load(arquivo)

    for pessoa in pessoas:
        p1 = Pessoa(**pessoas[0])
        p2 = Pessoa(**pessoas[1])
        p3 = Pessoa(**pessoas[2])

    print(p1.nome, p1.idade)
    print(p2.nome, p2.idade)
    print(p3.nome, p3.idade)
