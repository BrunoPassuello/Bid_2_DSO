from Posicao import Posicao
from Pessoa import Pessoa
from Cidade import Cidade
class Jogador(Pessoa):
    def __init__(self, nome : str, idade : int, cidade : Cidade, posicao : Posicao, altura : float, peso : float, estrangeiro : bool):
        super().__init__(nome, idade, cidade)
        self.__posicao = posicao
        self.__altura = altura
        self.__peso = peso
        self.__estrangeiro = estrangeiro
        self.__contrato = None
    
    @property
    def posicao(self):
        return self.__posicao
    
    @posicao.setter
    def posicao(self, posicao):
        self.__posicao = posicao
        
    @property
    def altura(self):
        return self.__altura
    
    @altura.setter
    def altura(self, altura):
        self.__altura = altura
        
    @property
    def peso(self):
        return self.__peso
    
    @peso.setter
    def peso(self, peso):
        self.__peso = peso
        
    @property
    def estrangeiro(self):
        return self.__estrangeiro
    
    @estrangeiro.setter
    def estrangeiro(self, estrangeiro):
        self.__estrangeiro = estrangeiro
        
    @property
    def contrato(self):
        return self.__contrato
    
    @contrato.setter
    def contrato(self, contrato):
        self.__contrato = contrato