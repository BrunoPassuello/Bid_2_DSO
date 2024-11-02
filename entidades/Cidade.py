from entidades.estado import Estado

class Cidade:
    def __init__(self, nome : str, estado : Estado):
        self.__nome = nome
        self.__estado = estado
    
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
    
    @property
    def estado(self):
        return self.__estado
    
    @estado.setter
    def estado(self, estado):
        self.__estado = estado
    