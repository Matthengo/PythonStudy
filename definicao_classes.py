'''
Uma classe serve para tratar cada objeto (instância) de forma única. Cada método aplicado à uma instância e atribuido um valor ao parâmetro fara o mesmo ser único àquele objeto.

Função vs Método
O método praticamente é uma função, mas dentro de uma classe.

self - Indica a instância que esta sendo utilizada.
Quando atribuimos uma classe à uma instância e aplicamos um método à essa instância, a classe sabe, atráves do self, que estamos aplicando o método à apenas uma instância.

objeto = ClassName()
objeto.metodo(self=objeto)

objeto: Instância/variável
ClassName() = Classe
.metodo() = Método da instância
objeto.metodo(self=objeto) → O self é o objeto e o "self=objeto" não é necessário, pois ja está implicito que o objeto é o self.
'''

class Pessoa:
    
    alguem_falando = False
    assunto_atual = ''

    def __init__(self, nome, idade, comendo=False, falando=False):
        self.nome = nome
        # self.nome fica disponível para todos os métodos da classe.
        self.idade = idade
        self.comendo = comendo
        self.falando = falando
        
    def falar(self, assunto):
        
        if self.comendo:
            print(f'{self.nome} não pode falar comendo.')
            return
        
        if Pessoa.alguem_falando and not self.falando:
            print(f'{self.nome} não pode falar pois alguém está falando.')
            return

        elif self.falando and self.assunto_atual == assunto:
            print(f'{self.nome} já está falando sobre {assunto}.')
            return

        print(f'{self.nome} está falando sobre {assunto}.')
        self.falando = True
        self.assunto_atual = assunto
        Pessoa.alguem_falando = True

    def parar_falar(self):
        if not self.falando:
            print(f'{self.nome} não está falando.')

        print(f'{self.nome} parou de falar sobre {self.assunto_atual}')
        self.falando = False
        Pessoa.alguem_falando = False
        

    def comer(self, alimento):
        if self.comendo:
            print(f'{self.nome} já está comendo.')
            return

        if self.falando:
            print(f'{self.nome} não pode comer falando.')
            return

        print(f'{self.nome} está comendo {alimento}.')
        self.comendo = True

    def parar_comer(self):
        if not self.comendo:
            print(f'{self.nome} não está comendo')
            return
        print(f'{self.nome} parou de comer.')
        self.comendo = False