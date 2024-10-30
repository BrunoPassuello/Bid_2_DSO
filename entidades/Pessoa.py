from abc import ABC, abstractmethod
from entidades.Pais import Pais
class Pessoa(ABC):
    
    @abstractmethod
    def __init__(self, nome : str, cpf : int, idade : int, pais : Pais):
        self.__nome = nome
        self.__cpf = cpf
        self.__idade = idade
        self.__pais = pais
    
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
    
    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf

    @property
    def idade(self):
        return self.__idade
    
    @idade.setter
    def idade(self, idade):
        self.__idade = idade
    
    @property
    def pais(self):
        return self.__pais
    
    @pais.setter
    def pais(self, pais):
        self.__pais = pais
    
