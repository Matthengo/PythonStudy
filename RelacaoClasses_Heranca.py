'''
Uma herança herda todos os métodos da sua classe ascendente

O método falar esta disponível para todos os descendentes de Pessoa
Mas o método estudar é único para aluno e comprar é unico para cliente
'''


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nomeclasse = self.__class__.__name__

    def falar(self):
        print(f'{self.nomeclasse} falando')


class Cliente(Pessoa):
    def comprar(self):
        print(f'{self.nomeclasse} comprando.')

    def falar(self):
        print('Estou em Cliente')


class Aluno(Pessoa):
    def estudar(self):
        print(f'{self.nomeclasse} estudando.')


print('------Cliente------')
c1 = Cliente('Matheus', 23)
c1.falar()
c1.comprar()
print()
print('------Aluno------')
a1 = Aluno('Cleber', 30)
a1.falar()
a1.estudar()


# Sobreposição
class ClienteVIP(Cliente):
    def __init__(self, nome, idade, sobrenome):
        super().__init__(nome, idade)
        self.sobrenome = sobrenome

    def falar(self):

        # super() chama o o descendente mais proximo
        # super().falar()
        Pessoa.falar(self)
        Cliente.falar(self)
        print('Outra coisa')


print()
print('------ClienteVIP------')
c2 = ClienteVIP('Rose', 25, 'Miranda')
c2.falar()

