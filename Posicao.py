class Posicao:
    def __init__(self, nome : str):
        self.nome = nome
    
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
    