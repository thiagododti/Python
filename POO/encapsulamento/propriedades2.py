class Pessoa:
    def __init__(self, nome, ano_nasc):
        self._nome = nome
        self._ano_nasc = ano_nasc

    @property
    def nome(self):
        return self._nome

    @property
    def idade(self):
        _ano_atual = 2024
        return _ano_atual - self._ano_nasc


pessoa = Pessoa("Thiago", 1992)

print(f"Nome: {pessoa.nome} \tIdade: {pessoa.idade}")

""" Em resumo, utilizamos o @property quando precisamos de uma informação
e não queremos armazenar ela necessariamente em uma variável como o exemplo
a cima
Em algum momento precisei da idade da pessoa, porém invés de eu armazenar
uma variável para colocar diretamente a idade, eu fiz uma forma dinâmica
utilizando um método e fazendo a consulta dele como um atributo invés de
chamar o método para fazer esse calculo da idade.
"""
