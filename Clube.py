from Jogador import Jogador
from Cidade import Cidade
from Tecnico import Tecnico
class Clube:
    def __init__(self, nome : str, cidade : Cidade):
        self.__nome = nome
        self.__jogadores = []
        self.__cidade = cidade
        self.__contrato_tecnico = None
    
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
        
    @property
    def contrato_tecnico(self):
        return self.__contrato_tecnico
    
    @contrato_tecnico.setter
    def tecnico(self, tecnico):
        self.__contrato_tecnico = tecnico
        
    def contratar_jogador(self, jogador : Jogador, salario : float, multa_rescisoria : float, contrato_produtividade : bool):
        from ContratoJogador import ContratoJogador
        contrato = ContratoJogador(self, jogador, salario, multa_rescisoria, contrato_produtividade)
        jogador.contrato = contrato
        self.__jogadores.append(contrato)
        
    def contratar_tecnico(self, tecnico : Tecnico, salario : float, multa_Rescisoria : float):
        from ContratoTecnico import ContratoTecnico
        contrato = ContratoTecnico(self, tecnico, salario, multa_Rescisoria)
        tecnico.contrato = contrato
        self.__contrato_tecnico = contrato
        