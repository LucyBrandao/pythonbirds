class Direcao:

    NORTE = 0
    LESTE = 1
    SUL = 2
    OESTE = 3

    DIRECOES = {
        NORTE: 'Norte',
        LESTE: 'Leste',
        SUL: 'Sul',
        OESTE: 'Oeste'
    }

    def __init__(self, direcao=NORTE):
        self.direcao = direcao

    def girar_a_direita(self):
        self.direcao = self.direcao + 1 if self.direcao < 3 else 0

    def girar_a_esquerda(self):
        self.direcao = self.direcao - 1 if self.direcao > 0 else 3

    def calcular_direcao(self):
        return self.DIRECOES[self.direcao]


if __name__ == '__main__':
    direcao = Direcao(direcao=Direcao.LESTE)
    print(Direcao.DIRECOES)
    print(Direcao.DIRECOES[direcao.direcao])
    direcao.girar_a_direita()
    print(Direcao.DIRECOES[direcao.direcao])
    direcao.girar_a_esquerda()
    print(Direcao.DIRECOES[direcao.direcao])
