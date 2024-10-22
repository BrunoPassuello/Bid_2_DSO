from Clube import Clube
from Jogador import Jogador
from Contrato import Contrato

class ContratoJogador (Contrato):
    def __init__(self, clube : Clube, jogador : Jogador, salario : float, multa_rescisoria : float, contrato_produtividade : bool):
        super().__init__(clube, salario, multa_rescisoria)
        self.__jogador = jogador
        self.__contrato_produtividade = contrato_produtividade
        if contrato_produtividade:
            self.salario = salario * 1.1
        
    @property
    def jogador(self):
        return self.__jogador
    
    @jogador.setter
    def jogador(self, jogador):
        self.__jogador = jogador
        
    @property
    def contrato_produtividade(self):
        return self.__contrato_produtividade
    
    @contrato_produtividade.setter
    def contrato_produtividade(self, contrato_produtividade):
        self.__contrato_produtividade = contrato_produtividade