from abc import ABC, abstractmethod, abstractproperty


class ControleRemoto(ABC):

    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

    # Podemos tambem fazer o contrato de propriedades
    @abstractproperty
    def marca(self):
        pass


class ControleTV(ControleRemoto):
    def ligar(self):
        print("Ligando TV...")

    def desligar(self):
        print("Desligando a TV...")

    @property
    def marca(self):
        return "LG"


tv = ControleTV()

tv.ligar()
tv.desligar()
print(tv.marca)
