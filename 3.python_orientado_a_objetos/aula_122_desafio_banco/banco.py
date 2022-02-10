class Banco:
    def __init__(self):
        self.agencias = [1111, 2222, 3333]
        self.contas = []
        self.clientes = []

    def inserir_conta(self, conta):
        self.contas.append(conta)

    def inserir_cliente(self, cliente):
        self.clientes.append(cliente)

    def autenticacao(self, cliente):
        if cliente not in self.clientes or cliente.conta not in self.contas or cliente.conta.agencia not in self.agencias:
            return False
        else:
            return True