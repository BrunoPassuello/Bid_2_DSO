class Licenca:
    def __init__(self, tipo : str):
        self.__tipo = tipo

    
    @property
    def tipo(self):
        return self.__tipo
    
    @tipo.setter
    def tipo(self, tipo):
        self.__tipo = tipo
