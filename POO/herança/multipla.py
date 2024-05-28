class Animal:
    def __init__(self, num_patas):

        self.num_patas = num_patas

    def esta_vivo(self):
        print("Está vivo!!")

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join(
            [f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


class Mamifero(Animal):
    def __init__(self, cor_pelo, **kw):
        super().__init__(**kw)

        self.cor_pelo = cor_pelo


class Ave(Animal):
    def __init__(self, cor_bico, **kw):
        super().__init__(**kw)

        self.cor_bico = cor_bico


class Ornitorrinco(Mamifero, Ave):
    def __init__(self, cor_pelo, cor_bico, num_patas):
        super().__init__(cor_pelo=cor_pelo,
                         cor_bico=cor_bico, num_patas=num_patas)
        # print(Ornitorrinco.__mro__)
        # print(Ornitorrinco.mro())


o = Ornitorrinco(num_patas=2, cor_pelo="Marron", cor_bico="Laranja")

print(o)

# O Python tem uma ordem de resolução de metodos, onde ele vai seguir
# uma ordem com base nas heranças

# Com o Exemplo a cima o python vai seguir
# a seguinte ordem para buscar os métodos

# 1° - vai resolver o método da classe filha - Ornitorrinco
# 2° Ele vai ler o a primeira classe Pai declarada - Mamifero
# 3° Ele vai ler a segunda classe Pai declarada - Ave
# 4° Vai finalmente resolver a classe originaria - Animal
# 5° Ele também vai buscar no objeto onde todas as classes estendem

# Ornitorrinco:
#              Mamífero:
#                       Ave:
#                           Animal:
#                                   Objeto:

# assim ele vai buscar o método esta vivo nessa ordem até ele encontrar
# o método na classe Animal.

# Obs: Se o mesmo método existir em todas as classes, ele vai executar
# somente o primeiro que for encontrado.

# Caso esteja com a duvida de como está a ordem das heranças codificadas
# basta usar o método mro() que ele vai exibir como está a ordem aplicada
# print(Ornitorrinco.__mro__)
# print(Ornitorrinco.mro())

print(Ornitorrinco.mro())
