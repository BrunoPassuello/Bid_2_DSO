from entidades.jogador import Jogador
from entidades.pais import Pais
from entidades.tecnico import Tecnico
from entidades.campeonato import Campeonato
class Clube:
    contador_id = 1  # Atributo de classe para gerar IDs únicos
    def __init__(self, nome: str, pais):
        self.id = Clube.contador_id
        Clube.contador_id += 1
        self.__nome = nome
        self.__pais = pais
        self.__jogadores = []          
        self.__contrato_tecnico = None  
        self.__campeonatos = [] 
        
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
    
    @property
    def pais(self):
        return self.__pais
    
    @pais.setter
    def pais(self, pais):
        self.__pais = pais

    @property
    def jogadores(self):
        return self.__jogadores
    
    @property
    def contrato_tecnico(self):
        return self.__contrato_tecnico
    
    @contrato_tecnico.setter
    def contrato_tecnico(self, contrato_tecnico):
        self.__contrato_tecnico = contrato_tecnico

    @property
    def campeonatos(self):
        return self.__campeonatos
