from definicao_classes import Pessoa

p1 = Pessoa('Matheus', 23)  # Criando um objeto a partir de uma classe (molde).
p2 = Pessoa('Marcos', 26)
# p1 pode ser chamado de instância.
# p1.nome = 'Matheus'  # .nome é um atributo.
'''
p1.comer('Kiwi')  # Está comendo
p1.comer('Kiwi')  # Já está comendo
p1.parar_comer()  # Parou de comer
p1.parar_comer()  # Não está comendo
p1.comer('Morango')  # Está comendo
p1.falar('POO')  # Não pode falar comendo
p1.parar_comer()  # Parou de comer
p1.falar('POO')  # Falando sobre
p1.falar('teste')  # Já esta falando
'''

p1.falar('POO')
p1.falar('POO')
p2.falar('POO')
p1.falar('Teste')
p1.parar_falar()
p2.falar('POO')

