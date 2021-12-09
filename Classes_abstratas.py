'''
Um método abstrato é um método que não tem corpo. Se cria o método para que as classes herdadas sejam obrigadas a criar tal método dentro de seu corpo. Se o método não for criado, haverá um erro dizendo que tal método não pode ser instanciado do herdeiro.
'''
from abc import ABC, abstractmethod

# Conceito

# A partir do momento que se cria um abstractmethod, a classe não pode mais ser instânciada.
class A(ABC):
    
    @abstractmethod
    def salario(self, parameter_list):
        pass

class PJ(A):
    # Sobrepondo a funcname
    def salario(self, parameter_list):
        pass
    def method1(self):
        pass

class PP(A):
    # Sobrepondo a funcname
    def salario(self, parameter_list):
        pass
    def method2(self):
        pass

class PS(A):
    # Sobrepondo a funcname
    def salario(self, parameter_list):
        pass
    def method3(self):
        pass


