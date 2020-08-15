class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome= None, idade=21):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'

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
    print(Pessoa.metodo_estatico(), leonardo.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), leonardo.nome_e_atributos_de_classe())
