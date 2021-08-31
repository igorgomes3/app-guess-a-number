import time
import random
from os import system

class ChuteNumber:
    def __init__(self):
        self.aleatorio = 0
        self.minimo = 0
        self.maximo = 100
        self.chute = 0

    def Iniciar(self):
        self.aleatorio = self.GerarRandom()
        self.Perguntar()
        while self.aleatorio != self.chute:
            if self.aleatorio > self.chute:
                system('clear')
                print(f'Você chutou >> {self.chute}')
                print('Chute um número maior...')
                print('--------------------\n')
                self.Perguntar()
            elif self.aleatorio < self.chute:
                system('clear')
                print(f'Você chutou >> {self.chute}')
                print('Chute um número menor...')
                print('--------------------\n')
                self.Perguntar()
        system('clear')
        print('\nParabéns, você acertou!')
        time.sleep(1)
        print(f'Número certo >>> {self.aleatorio}\n')

    def Perguntar(self):
        try:
            self.chute = int(
                input(f'\nChute um número entre {self.minimo} e {self.maximo}:\n>>> ')
            )
        except ValueError:
            print('\nPor favor digite apenas números...\n')
            self.Perguntar()

    def GerarRandom(self):
        return random.randint(self.minimo, self.maximo)


auto = ChuteNumber()
auto.Iniciar()