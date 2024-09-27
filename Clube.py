from Jogador import Jogador
class Clube:
    def __init__(self, nome : str):
        self.nome = nome
        self.jogadores = []
    
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
        
    
    