class CarrinhoDeCompras():
    def __init__(self):
        self.produtos = []

    def inserir_produto(self, produto):
        self.produtos.append(produto)

    def lista_produtos(self):
        for produto in self.produtos:
            print(produto.nome, produto.preco)

    def soma_total(self):
        total = 0
        for produto in self.produtos:
            total += produto.preco
        return total

class Produto():
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco


p1 = Produto('vassoura', 10)
p2 = Produto('sabão', 2)
p3 = Produto('biscoito', 5)

carrinho = CarrinhoDeCompras()

carrinho.inserir_produto(p1)
carrinho.inserir_produto(p3)
carrinho.inserir_produto(p2)
carrinho.inserir_produto(p3)

carrinho.lista_produtos()
print(carrinho.soma_total())