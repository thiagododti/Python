class Camera:
    # declarando assim eu defino um estado da instancia
    def __init__(self, nome, filmando=False):
        self.nome = nome
        self.filmando = filmando  # estado da instância

    def filmar(self):
        if self.filmando:
            print(f'{self.nome} Já está filmando.')
            return

        print(f'{self.nome} está filmando')
        self.filmando = True  # e através dos metodos eu defino o estado da utilização do objeto

    def Parar_Filmar(self):
        if not self.filmando:
            print(f'{self.nome} Não Está filmando')
            return

        print(f'{self.nome}  parou de filmar.')
        self.filmando = False


c1 = Camera('Canon')

c1.filmar()
c1.Parar_Filmar()
