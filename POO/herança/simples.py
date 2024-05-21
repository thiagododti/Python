# Herança Simples

class Veiculo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas

    def ligar_motor(self):
        print("Ligando o motor")


class Motocicleta(Veiculo):
    pass


class Carro(Veiculo):
    pass


class Caminhao(Veiculo):
    def __init__(self, cor, placa, numero_rodas, peso):
        # aqui eu chamo os atributos da classe pai
        super().__init__(cor, placa, numero_rodas)
        self.peso = peso

    def peso_carregamento(self):
        print(f"Peso do caminhão: {self.peso}kg")


moto = Motocicleta("Azul", "OVP1111", 2)
carro = Carro("Vermelho", "OVP2222", 4)
caminhao = Caminhao("Preto", "OVP3333", 6, 50)

print(moto.cor)
print(carro.cor)
print(caminhao.cor)
caminhao.peso_carregamento()
