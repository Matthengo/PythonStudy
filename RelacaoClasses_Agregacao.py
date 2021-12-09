'''
Agregação é como se fosse uma associação, mas uma classe depende da outra para ter seu devido funcionamento.
Ambas existem sozinhas.
Nesse caso a Classe Produto funciona sozinha, mas a CarrinhoCompras "depende" da Produto para poder ter sua execução devida.
'''
class CarrinhoCompras:
    
    # O construtor recebe um parametro chamado self.produtos
    def __init__(self):
        self.produtos = []

    # Insere um produto ao carrinho
    def inserir_produto(self, produto):
        self.produtos.append(produto)

    # Lista os produtos do carrinho
    def lista_produto(self):
        for produto in self.produtos:
            print(produto.nome, produto.valor)

    # Faz uma soma total dos produtos
    def soma_total(self):
        total = 0
        for produto in self.produtos:
            total += produto.valor
        return total

# Classe que será usada como agregação à CarrinhoCompras
class Produto:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor

# Criando instâncias diferentes de Produto
p1 = Produto("Camiseta", 30)
p2 = Produto("Caneca", 40)
p3 = Produto("Poster", 60)

# Criando a instância de CarrinhoCompras
carrinho = CarrinhoCompras()
# A classe CarrinhoCompras insere o produto da classe Produto
carrinho.inserir_produto(p1)
carrinho.inserir_produto(p2)
carrinho.inserir_produto(p3)
carrinho.inserir_produto(p2)
carrinho.inserir_produto(p1)

carrinho.lista_produto()

print(carrinho.soma_total())