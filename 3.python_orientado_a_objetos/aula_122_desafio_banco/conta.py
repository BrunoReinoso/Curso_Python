from abc import ABC, abstractmethod

class Conta(ABC):
    """Esta classe precisa de abstração para garantir o método 
    "sacar" nas filhas e também pois não é recomendada sua instanciação"""

    def __init__(self, agencia, numero_conta, saldo = 0):
        super().__init__()
        self.agencia = agencia
        self.conta = numero_conta
        self.saldo = saldo

    @abstractmethod
    def sacar(self, valor):
        pass

    def depositar(self, valor):
        self.saldo += valor
        print(f'Você fez um depósito de {valor}.\n'
              f'Seu saldo atual é de {self.saldo}.')

    def detalhes(self):
        print(f'Agência: {self.agencia}\n'
              f'Conta: {self.conta}\n'
              f'Saldo: {self.saldo}')

class ContaPoupanca(Conta):
    def __init__(self, agencia, numero_conta, saldo=0):
        super().__init__(agencia, numero_conta, saldo)
    
    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            print(f'Você fez um saque de {valor}.\n'
                  f'Seu saldo atual é de {self.saldo}')
        else:
            print(f'Não é possível sacar o valor de {valor} pois você possui em conta R${self.saldo}')

class ContaCorrente(Conta):
    def __init__(self, agencia, numero_conta, saldo=0, limite = 100):
        super().__init__(agencia, numero_conta, saldo)
        self.limite = limite
    
    def sacar(self, valor):
        if self.saldo + self.limite >= valor:
            self.saldo -= valor

        else:
            print(f'Não é possível sacar o valor de {valor} pois você possui em conta R${self.saldo} e seu limite é de R${self.limite}.')
