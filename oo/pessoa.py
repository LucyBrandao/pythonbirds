class Pessoa:
    olhos = 2

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
    leonardo.sobrenome = 'Santos'
    del leonardo.filhos
    leonardo.olhos = 1
    del leonardo.olhos
    print(leonardo.__dict__)
    print(marcos.__dict__)
    Pessoa.olhos = 3
    print(Pessoa.olhos)
    print(leonardo.olhos)
    print(marcos.olhos)
    print(id(Pessoa.olhos), id(leonardo.olhos), id(marcos.olhos))
