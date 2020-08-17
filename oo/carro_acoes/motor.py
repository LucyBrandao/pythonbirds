class Motor:

    velocidade = 0

    def acelerar(self):
        self.velocidade += 1

    def frear(self):
        self.velocidade = 0 if self.velocidade - 2 < 0 else self.velocidade - 2

    def calcular_velocidade(self):
        return self.velocidade


if __name__ == '__main__':
    motor = Motor()
    print(f'velocidade: {motor.velocidade}')
    motor.acelerar()
    print(f'velocidade: {motor.velocidade}')
    motor.acelerar()
    print(f'velocidade: {motor.velocidade}')
    motor.acelerar()
    print(f'velocidade: {motor.velocidade}')
    motor.frear()
    print(f'velocidade: {motor.velocidade}')
    motor.frear()
    print(f'velocidade: {motor.velocidade}')

