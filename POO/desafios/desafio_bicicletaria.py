class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print("Plim Plim")

    def parar(self):
        print("Parando a bicicleta...")
        print("Bicicleta parou!")

    def correr(self):
        print("Acelerou!")

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join(
            [f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


b = Bicicleta("Amarela", "Caloi", 2024, 1000.00)

b.buzinar()

print(b)
