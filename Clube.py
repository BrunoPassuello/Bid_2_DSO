from Jogador import Jogador
class Clube:
    def __init__(self, nome : str):
        self.__nome = nome
        self.__jogadores = []
    
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
        
    def contratar_jogador(self, jogador : Jogador, salario : float, multa_rescisoria : float, contrato_produtividade : bool):
        from ContratoJogador import ContratoJogador
        contrato = ContratoJogador(self, jogador, salario, multa_rescisoria, contrato_produtividade)
        jogador.contrato = contrato
        self.__jogadores.append(jogador)