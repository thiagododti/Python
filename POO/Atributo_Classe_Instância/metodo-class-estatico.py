class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    # Utilizamos o decorador para definirmos um método de classe
    # e como convenção cls invés de self
    @classmethod
    def criar_de_data_nasc(cls, ano, mes, dia, nome):
        idade = 2024 - ano
        return Pessoa(nome, idade)

    # E a mesma coisa para método estático através do decorador
    @staticmethod
    def e_maior_idade(idade):
        return idade >= 18


# utilizando método de classe
p = Pessoa.criar_de_data_nasc(1992, 3, 21, "Thiago")

# utilizando método estático
print(Pessoa.e_maior_idade(9))  # False
