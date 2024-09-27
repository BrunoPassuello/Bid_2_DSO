from Jogador import Jogador
from Cidade import Cidade
class Clube:
    def __init__(self, nome : str, cidade : Cidade):
        self.__nome = nome
        self.__jogadores = []
        self.__cidade = cidade
    
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
        
    @property
    def jogadores(self):
        return self.__jogadores
    
    @property
    def cidade(self):
        return self.__cidade
    
    @cidade.setter
    def cidade(self, cidade):
        self.__cidade = cidade
        
    def contratar_jogador(self, jogador : Jogador, salario : float, multa_rescisoria : float, contrato_produtividade : bool):
        from ContratoJogador import ContratoJogador
        contrato = ContratoJogador(self, jogador, salario, multa_rescisoria, contrato_produtividade)
        jogador.contrato = contrato
        self.__jogadores.append(jogador)