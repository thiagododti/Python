class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print("Peeeeeeemmmm")

    def parar(self):
        print("Parou")

    def correr(self):
        print("Acelerou!")


b = Bicicleta("Amarela", "Caloi", "2024", "1000.00")

b.buzinar()

print(b.cor)
