'''
A composição faz com que uma classe dependa totalmente de outra classe. Se a instância da classe "mestre" for excluida, as informações da classe "servo" também serão.

No caso abaixo a classe endereço esta entrelaçada com a classe cliente. Se a instancia criada para cliente for excluida, as informações de endereco também serão.
'''
class Cliente:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.enderecos = []

    # Insere diretamente as informações da classe Endereco juntamente com as informações do cliente
    def insere_endereco(self, cidade, estado):
        self.enderecos.append(Endereco(cidade, estado))

    def lista_enderecos(self):
        for endereco in self.enderecos:
            print(endereco.cidade, endereco.estado)

    # Esse método só foi chamado para mostrar que quando o cliente for deletado, a cidade/estado também serão
    def __del__(self):
        print(f'{self.nome} FOI APAGADO')


class Endereco:
    def __init__(self, cidade, estado):
        self.cidade = cidade
        self.estado = estado
        
    # Esse método só foi chamado para mostrar que quando o cliente for deletado, a cidade/estado também serão
    def __del__(self):
        print(f'{self.cidade}/{self.estado} FOI APAGADO')


cliente1 = Cliente('Luiz', 32)
cliente1.insere_endereco('Belo Horizonte', 'MG')
print(cliente1.nome)
cliente1.lista_enderecos()
del cliente1
print()

cliente2 = Cliente('Maria', 55)
cliente2.insere_endereco('Salvador', 'BA')
cliente2.insere_endereco('Rio de Janeiro', 'RJ')
print(cliente2.nome)
cliente2.lista_enderecos()
del cliente2
print()

cliente3 = Cliente('João', 19)
cliente3.insere_endereco('São Paulo', 'SP')
print(cliente3.nome)
cliente3.lista_enderecos()
del cliente3
print()