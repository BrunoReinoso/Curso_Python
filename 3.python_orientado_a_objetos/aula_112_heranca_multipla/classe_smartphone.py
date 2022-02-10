from classe_eletronico import Eletronico
from classe_log import Log

class Smartphone(Eletronico, Log):
    def __init__(self, modelo):
        super().__init__()
        self.modelo = modelo
        self.conectado = False

    def ligar_internet(self):
        if self.conectado == True:
            msg = 'O aparelho já está conectado.'
            Log.escreve(msg, 0)
            return

        self.conectado = True
        msg = 'O aparelho está conectado.'
        Log.escreve(msg, 1)
        

    def desligar_internet(self):
        if self.conectado == False:
            msg = 'O aparelho já está desconectado.'
            Log.escreve(msg, 0)
            return

        self.conectado = False
        msg = 'O aparelho está desconectado.'
        Log.escreve(msg, 1)

    def info(self):
        msg = 'Modelo atual: ' + self.modelo
        Log.escreve(msg, 1)