class Foo:
    def __init__(self, x=None):
        self._x = x

    @property
    def x(self):
        return self._x or 0

    # para alterar o valor precisa ter um setter para essa propriedade
    @x.setter
    def x(self, value):
        self._x += value

    @x.deleter
    def x(self, value):
        self._x = 0


foo = Foo(10)

print(foo.x)  # invés de chamar como método, chamo como a sintaxe de atributo

# assim ele vai executar o comando dentro do método e vou acessa-lo
# o resultado diretamente como atributo
