class Cachorro:
    # Método construtor

    """ O método construtor sempre é executado quando uma nova
    instância da classe é criada. Nesse método inicializamos
    o estado do nosso objeto. Para declarar o método construtor
    da classe, criamos um método com o nome __init__.
    """

    def __init__(self, nome, cor, acordado=True):
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    # Método destrutor

    """ O método destrutor sempre é executado quando uma instância é
    destruída. Destrutores em Python não são tão necessários quanto em C++
    porque o Python tem um coletor de lixo que lida com o gerenciamento
    de memória automaticamente. Para declarar o método destrutor da classe,
    criamos um método com o nome __del__.
    """

    def __del__(self):
        print("Destruindo a instância")


c = Cachorro("Dog", "Marron")

print(c.nome)  # Após executar a instancia e destruida

# e para forçar a destruição de uma instancia antes de acabar toda execução
# basta usar o comando del com o nome da instancia que deseja destruir.add()

del c
