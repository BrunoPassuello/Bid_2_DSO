from abc import ABC, abstractmethod
from Cidade import Cidade
class Pessoa(ABC):
    
    @abstractmethod
    def __init__(self, nome : str, idade : int, cidade : Cidade):
        self.__nome = nome
        self.__idade = idade
        self.__cidade = cidade
    
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
    
    @property
    def idade(self):
        return self.__idade
    
    @idade.setter
    def idade(self, idade):
        self.__idade = idade
    
    @property
    def cidade(self):
        return self.__cidade
    
    @cidade.setter
    def cidade(self, cidade):
        self.__cidade = cidade
    
