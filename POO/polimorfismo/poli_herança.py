class Passaro:
    def voar(self):
        print("Voando...")


class Pardal(Passaro):
    def voar(self):
        return super().voar()


class Avestruz(Passaro):
    def voar(self):
        print("Não consegue voar")

# para criar o polimorfismo em plano_voo eu passo o objeto como parametro
# para utilizar a método voar que possui resultados diferentes em cada classe

# dessa forma nao preciso criar o plano_voo em cada classe, e sim um método só
# para se utilizar do método de cada classe


def plano_voo(obj):
    obj.voar()


plano_voo(Pardal())
plano_voo(Avestruz())
