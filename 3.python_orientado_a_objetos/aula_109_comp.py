class Cliente:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.enderecos = []
        
    def inserir_endereco(self, cidade, estado):
        self.enderecos.append(Endereco(cidade, estado))

    def lista_enderecos(self):
        for endereco in self.enderecos:
            print(f'{endereco.cidade} - {endereco.estado}')

    def perfil(self):
        print(f'Cliente: {self.nome}\nIdade: {self.idade} anos')

    def __del__(self):
        print(f'{self.nome} DELETADO')

class Endereco():
    def __init__(self, cidade, estado):
        self.cidade = cidade
        self.estado = estado

    def __del__(self):
        print(f'{self.cidade} - {self.estado} DELETADO')

cliente1 = Cliente('Bruno', 25)
cliente1.inserir_endereco('Rio das Ostras', 'RJ')

cliente1.perfil()
cliente1.lista_enderecos()
del cliente1