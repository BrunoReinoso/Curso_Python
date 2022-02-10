from banco import Banco
from individuo import Cliente
from conta import ContaCorrente, ContaPoupanca

banco = Banco()

cliente1 = Cliente('Bruno', 25)
cliente2 = Cliente('Eduarda', 23)
cliente3 = Cliente('Gabriel', 24)

conta1 = ContaPoupanca(1111, 12345)
conta2 = ContaCorrente(2222, 12346, 10)
conta3 = ContaPoupanca(3333, 12347, 50)

cliente1.inserir_conta(conta1)
cliente2.inserir_conta(conta2)
cliente3.inserir_conta(conta3)

banco.inserir_conta(conta1)
banco.inserir_conta(conta2)
banco.inserir_conta(conta3)

banco.inserir_cliente(cliente1)
banco.inserir_cliente(cliente2)
banco.inserir_cliente(cliente3)


if banco.autenticacao(cliente3):
    cliente3.conta.depositar(10)
    cliente3.conta.depositar(10)
    cliente3.conta.depositar(10)
    cliente3.conta.sacar(24)
else:
    print(f'Erro de autenticação')