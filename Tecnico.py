from Licenca import Licenca
from Pessoa import Pessoa
class Tecnico(Pessoa):
    def __init__(self, nome : str, idade : int, cidade, licenca : Licenca):
        super().__init__(nome, idade, cidade)
        self.__licenca = licenca
        
    @property
    def licenca(self):
        return self.__licenca
    
    @licenca.setter
    def licenca(self, licenca):
        self.__licenca = licenca
