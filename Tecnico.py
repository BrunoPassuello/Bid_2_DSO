from Licenca import Licenca
from Pessoa import Pessoa
class Tecnico(Pessoa):
    def __init__(self, nome : str, idade : int, cidade, licenca : Licenca):
        super().__init__(nome, idade, cidade)
        self.__licenca = licenca
        self.__contrato = None
        
    @property
    def licenca(self):
        return self.__licenca
    
    @licenca.setter
    def licenca(self, licenca):
        self.__licenca = licenca

    @property
    def contrato(self):
        return self.__contrato
    
    @contrato.setter
    def contrato(self, contrato):
        self.__contrato = contrato