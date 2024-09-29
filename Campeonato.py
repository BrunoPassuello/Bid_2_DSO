from Regra import Regra

class Campeonato:
    def __init__(self, nome : str, premiacao : float, numero_times : int, numero_estrangeiros : int, numero_jogadores : int):
        self.__nome = nome
        self.__premiacao = premiacao
        self.__regra = Regra(numero_times, numero_estrangeiros, numero_jogadores)
        self.__clubes = []
    
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
        
    @property
    def premiacao(self):
        return self.__premiacao
    
    @premiacao.setter
    def premiacao(self, premiacao):
        self.__premiacao = premiacao
        
    @property
    def regra(self):
        return self.__regra
    
    @regra.setter
    def regra(self, regra):
        self.__regra = regra
        
    @property
    def clubes(self):
        return self.__clubes
    
    @clubes.setter
    def clubes(self, clubes):
        self.__clubes = clubes
    
    def listar_clubes(self):
        if len(self.__clubes) > 0:
            clubes_ordenados = sorted(self.__clubes, key = lambda clube: clube.nome)
            for clube in clubes_ordenados:
                print(clube.nome)
    