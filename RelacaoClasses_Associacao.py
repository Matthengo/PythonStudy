class Escritor:
    def __init__(self, nome):
        self.__nome = nome
        self.__ferramenta = None

    @property
    def nome(self):
        return self.__nome
    # Apesar do atributo nome estar como privado, não é necessário deixa-lo como privado. Nesse exemplo está apenas para reformar o uso do privado.

    @property
    def ferramenta(self):
        return self.__ferramenta

    # Neste Setter está sendo criado uma Associação entre classes. Associa-se NomeIntanciaEscritor.ferramenta = NomeInstanciaCaneta. Depois chama NomeInstanciaEscritor.ferramenta.escrever(). Isso indica que a instância da classe Escritor está chamando um método de instância da classe Caneta.
    # PS: O nome é ferramenta, mas pode ser qualquer outro nome de atributo associativo.
    @ferramenta.setter
    def ferramenta(self, ferramenta):
        self.__ferramenta = ferramenta

class Caneta:
    def __init__(self, marca):
        self.__marca = marca

    @property
    def marca(self):
        return self.__marca

    def escrever(self):
        print("Caneta está escrevendo.")


print("-----------Associação-----------")
print()
e1 = Escritor('Cleber')
c1 = Caneta('Mont Blanc')
e1.ferramenta = c1
e1.ferramenta.escrever()