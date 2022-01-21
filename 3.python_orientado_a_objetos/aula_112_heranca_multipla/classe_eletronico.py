from classe_log import Log

class Eletronico(Log):
    def __init__(self):
        self.ligado = False

    def ligar(self):
        if self.ligado == True:
            msg = 'O aparelho já está ligado.'
            Log.escreve(msg, 0)
            return

        self.ligado = True
        msg = 'O aparelho ligou.'
        Log.escreve(msg, 1)

    def desligar(self):
        if self.ligado == False:
            msg = 'O aparelho já está desligado.'
            Log.escreve(msg, 0)
            return

        self.ligado = False
        msg = 'O aparelho desligou.'
        Log.escreve(msg, 1)