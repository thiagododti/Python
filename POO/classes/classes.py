# class - Classes são moldes para criar novos objetos
# As classes geram novos objetos (instancias) que
# podem ter seus próprios atributos e métodos.
# Os objetos gerados pela classe podem usar seus dados
# internos para realizar várias ações.
# Por convenção, usamos PascalCase para nomes de classes
# Hard coded - É algo que foi escrito diretamente na classe! self.nome = 'Thiago'
# assim toda classe vai ter o mesmo nome atribuído nela.

class Pessoa:  # Nome da nossa Classe
    def __init__(self, nome):  # Construtor é um método especial chamado assim
        self.nome = nome  # At


p1 = Pessoa('Thiago')

print(p1.nome)  # Thiago

# Métodos

# Classe - Molde (geralmente sem dados)
# Instância da class (objeto) - Tem os dados
# Uma classe pode gerar várias instâncias.
# Na classe o self é a própria instância.


class Carro:
    def __init__(self, marca):
        self.marca = marca

    def acelerar(self):
        print(f'{self.marca} está acelerando...')


fusca = Carro('Fusca')

print(fusca.marca)
fusca.acelerar()
