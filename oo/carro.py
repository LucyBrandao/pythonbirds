"""
Criar uma classe carro que vai possuir dois atributos compostos de outras duas classes:

1) Motor
2) Direção

O Motor terá a responsabilidade de controlar a velocidade.
Ele oferece os seguintes atributos:
1) Atributo de dado velocidade
2) Método de acelerar, que deverá incrementar a velocidade de uma unidade
3) Método frear que deverá decrementar a velocidade em duas unidades

A direção terá a responsabilidade de controlar a direção. Ela oferecerá os seguintes valores:
1) Valor de direção com valores possíbeis: Norte, Sul, Leste, Oeste.
2) Métodos girar_a_direita
3) Métodos girar_a_esquerda

  N
O   L
  S

  Exemplo:
  >>> # Testando motor
  >>> motor = Motor()
  >>> motor.velocidade
  0
  >>> motor.acelerar()
  >>> motor.velocidade
  1
  >>> motor.acelerar()
  >>> motor.velocidade
  2
  >>> motor.acelerar()
  >>> motor.velocidade
  3
  >>> motor.frear()
  >>> motor.velocidade
  1
  >>> motor.frear()
  >>> motor.velocidade
  0
  >>> # Testando direção
  >>> direcao = Direcao()
  >>> direcao.valor
  'Norte'
  >>> direcao.girar_a_direita()
  >>> direcao.valor
  'Leste'
  >>> direcao.girar_a_direita()
  >>> direcao.valor
  'Sul'
  >>> direcao.girar_a_direita()
  >>> direcao.valor
  'Oeste'
  >>> direcao.girar_a_direita()
  >>> direcao.valor
  'Norte'
  >>> direcao.girar_a_esquerda()
  >>> direcao.valor
  'Oeste'
  >>> direcao.girar_a_esquerda()
  >>> direcao.valor
  'Sul'
  >>> direcao.girar_a_esquerda()
  >>> direcao.valor
  'Leste'
  >>> direcao.girar_a_esquerda()
  >>> direcao.valor
  'Norte'
  >>> carro = Carro(direcao, motor)
  >>> carro.calcular_velocidade()
  0
  >>> carro.acelerar()
  >>> carro.calcular_velocidade()
  1
  >>> carro.acelerar()
  >>> carro.calcular_velocidade()
  2
  >>> carro.frear()
  >>> carro.calcular_velocidade()
  0
  >>> carro.calcular_direcao()
  'Norte'
  >>> carro.girar_a_direita()
  >>> carro.calcular_direcao()
  'Leste'
  >>> carro.girar_a_esquerda()
  >>> carro.calcular_direcao()
  'Norte'
  >>> carro.girar_a_esquerda()
  >>> carro.calcular_direcao()
  'Oeste'

"""
from oo.carro_acoes.motor import Motor
from oo.carro_acoes.direcao import Direcao


class Carro(Motor, Direcao):
    pass


if __name__ == '__main__':
    carro = Carro()
    print(carro.calcular_velocidade())
    carro.acelerar()
    print(carro.calcular_velocidade())
    carro.acelerar()
    print(carro.calcular_velocidade())
    carro.frear()
    print(carro.calcular_velocidade())
    carro.girar_a_direita()
    print(carro.calcular_direcao())
    carro.girar_a_direita()
    print(carro.calcular_direcao())
    carro.girar_a_esquerda()
    print(carro.calcular_direcao())
