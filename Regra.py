class Regra:
    def __init__(self, numero_times : int, numero_estrangeiros : int, numero_jogadores : int):
        self.__numero_times = numero_times
        self.__numero_estrangeiros = numero_estrangeiros
        self.__numero_jogadores = numero_jogadores
    
    @property
    def numero_times(self):
        return self.__numero_times
    
    @numero_times.setter
    def numero_times(self, numero_times):
        self.__numero_times = numero_times
        
    @property
    def numero_estrangeiros(self):
        return self.__numero_estrangeiros
    
    @numero_estrangeiros.setter
    def numero_estrangeiros(self, numero_estrangeiros):
        self.__numero_estrangeiros = numero_estrangeiros
        
    @property
    def numero_jogadores(self):
        return self.__numero_jogadores
    
    @numero_jogadores.setter
    def numero_jogadores(self, numero_jogadores):
        self.__numero_jogadores = numero_jogadores