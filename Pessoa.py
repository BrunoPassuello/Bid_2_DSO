from abc import ABC, abstractmethod
class Pessoa(ABC):
    
    @abstractmethod
    def __init__(self, nome : str, idade : int):
        self.nome = nome
        self.idade = idade
    
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
    
