class Licenca:
    def __init__(self, tipo : str, ano : int):
        self.__tipo = tipo
        self.__ano = ano
    
    @property
    def tipo(self):
        return self.__tipo
    
    @tipo.setter
    def tipo(self, tipo):
        self.__tipo = tipo
        
    @property
    def ano(self):
        return self.__ano
    
    @ano.setter
    def ano(self, ano):
        self.__ano = ano
