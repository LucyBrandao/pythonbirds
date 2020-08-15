class Pessoa:
    def __init__(self, *filhos, nome= None, idade=21):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    marcos = Pessoa(nome='Marcos')
    leonardo = Pessoa(marcos, nome='Leonardo')
    print(Pessoa.cumprimentar(leonardo))
    print(id(leonardo))
    print(leonardo.cumprimentar())
    print(leonardo.nome)
    print(leonardo.idade)
    for filho in leonardo.filhos:
        print(filho.nome)
