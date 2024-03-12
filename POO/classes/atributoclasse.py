# Atributo de classe

""" quando se precisa usar um atributo que so é necessário para a classe
podemos gerar um atributo de classe, assim esse atributo só sera utilizado
dentro dessa classe sem a necessidade de declararmos ela fora da mesma porém
podemos acessar esse atributo fora dela caso precise.
"""


class Pessoa:
    ANO_ATUAL = (2024,)  # atributo de classe declarado

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def anoNascimento(self):
        # utilização do atributo dentro da classe
        return Pessoa.ANO_ATUAL[0] - self.idade


# tentativa de alterar uma constante definida como tupla para nao ter alteração fora da classe
Pessoa.ANO_ATUAL[0] = 1

Thiago = Pessoa('Thiago', 31)

print(Pessoa.ANO_ATUAL[0])  # podemos acessar o atributo fora da classe também
print(Thiago.anoNascimento())
