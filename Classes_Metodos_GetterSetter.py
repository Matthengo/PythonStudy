'''
objeto = ClassName()
objeto.metodo(self=objeto)

objeto: Instância/variável
ClassName() = Classe
.metodo() = Método da instância
objeto.metodo(self=objeto) → O self é o objeto e o "self=objeto" não é necessário, pois ja está implicito que o objeto é o self.

Encapsulamento
_ : Indica que um objeto não pode ser acessado/alterado, mas é visível
__ : Indica fortemente que um objeto não pode ser acessado/alterado. Não é visível. Quando é alterado, o Python cria um nome de segurança chamado _ClassName__objeto, sendo o original. O alterado não é o original.
'''
# O objetivo de uma classe é tratar cada objeto (variável/instância) de forma única.
class Pessoa:
    ano_atual = 2020
    assunto_atual = ''
    alguem_falando = False
    # Variável/Atributo de Classe. É uma variável que pode ser acessada e mudada pela classe em si, fazendo ser mudada para todas as intâncias, ou ser acessada e mudada por uma instância em específico, sendo mudada apenas para ela mesma.

    # No construtor __init__ encontra-se o self e os parâmetros. Esses parametros serão únicos para cada atributo moldado.
    # O self serve para indicar à classe que uma instância esta sendo utilizada.
    def __init__(self, nome, idade, falando=False):
    # Construtor inicializador para as instãncias.    
        self.nome = nome
        # self.nome fica disponível para todos os métodos da classe.
        self.idade = idade
        self.falando = falando

    # Getter
    # O getter pega um atributo, fazendo uma propriedade do mesmo e cria um filtro, retornando ela com outro nome.
    @property
    def idade(self):
        return self._idade

    # Setter
    # O Setter pega o atributo modificado no getter e formata ele sem mexer na estrutura do construtor.
    @idade.setter
    def idade(self, idade):
        if isinstance(idade, str):
            idade = int(idade.replace(' anos', ''))
        self._idade = idade
    
    # Método de instância irá fazer a instância executar uma função determinada pelo método quando ela for chamada
    def falar(self, assunto):
        if Pessoa.alguem_falando and not self.falando:
            print(f'{self.nome} não pode falar pois alguém está falando.')
            return
        
        elif self.falando and self.assunto_atual == assunto:
            print(f'{self.nome} já está falando sobre {assunto}.')
            return

        print(f'{self.nome} está falando sobre {assunto}.')
        self.falando = True
        
        # Variável de classe sendo alterada para a instância.
        self.assunto_atual = assunto

        # Variável de classe sendo alterada para a classe.
        Pessoa.alguem_falando = True

    # Método de classe se delimita à classe em vez do objeto. Não é necessário a criação de uma instancia de classe. No caso abaixo ele pega os dados da pessoa através do ano de nascimento.
    @classmethod
    def ano_nascimento(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)

    # Métodos estáticos são que nem funções fora de uma classe. Não necessitam de cls ou self. São independentes da classe ou instância.
    @staticmethod
    def mensagem():
        return f'Bem-vindo'





p1 = Pessoa("Matheus", 23)
p2 = Pessoa("Max", '28 anos')
print("--------Objeto moldado--------")
print(p1.nome, p1.idade)
print(p2.nome, p2.idade)
print()
print("-------Método de Classe-------")
print()
p3 = Pessoa.ano_nascimento("Jorge", 1993)
# p3 está chamando o método de classe ano_nascimento delimitado pela classe Pessoa.
print(p3.nome, p3.idade)
print()
print("-------Método Estático-------")
print()
print(Pessoa.mensagem())
print()
print("------Método de instância------")
print()
p1.falar("POO")  # Fala sobre
p2.falar("Teste")  # Alguem ja esta falando
p1.falar("POO")  # Ja está falando
print()


