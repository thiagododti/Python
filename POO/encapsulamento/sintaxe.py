class Conta:
    def __init__(self, saldo=0):
        self._saldo = saldo  # iniciando com _ definimos que é privado

    def depositar(self, valor):

        self._saldo += valor

    def sacar(self, valor):
        self._saldo -= valor

    def mostrar_saldo(self):    # Para acessar uma variável privada
        return self._saldo      # definimos um método


conta = Conta(500)

print(conta._saldo)  # acesso incorreto da variável

print(conta.mostrar_saldo())  # acesso correto da variável
