from Clube import Clube
from Jogador import Jogador


class ContratoJogador:
    def __init__(self, clube : Clube, jogador : Jogador, salario : float, multa_rescisoria : float, contrato_produtividade : bool):
        self.__clube = clube
        self.__jogador = jogador
        self.__salario = salario
        self.__multa_rescisoria = multa_rescisoria
        self.__contrato_produtividade = contrato_produtividade
        if contrato_produtividade:
            self.salario = salario * 1.1
    
    @property
    def clube(self):
        return self.__clube
    
    @clube.setter
    def clube(self, clube):
        self.__clube = clube
        
    @property
    def jogador(self):
        return self.__jogador
    
    @jogador.setter
    def jogador(self, jogador):
        self.__jogador = jogador
        
    @property
    def salario(self):
        return self.__salario
    
    @salario.setter
    def salario(self, salario):
        self.__salario = salario
    
    @property
    def multa_rescisoria(self):
        return self.__multa_rescisoria

    @multa_rescisoria.setter
    def multa_rescisoria(self, multa_rescisoria):
        self.__multa_rescisoria = multa_rescisoria
        
    @property
    def contrato_produtividade(self):
        return self.__contrato_produtividade
    
    @contrato_produtividade.setter
    def contrato_produtividade(self, contrato_produtividade):
        self.__contrato_produtividade = contrato_produtividade
    