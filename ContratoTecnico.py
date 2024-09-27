from Clube import Clube
from Tecnico import Tecnico

class ContratoTecnico:
    def __init__(self, clube : Clube, tecnico : Tecnico, salario : float, multa_rescisoria : float):
        self.__clube = clube
        self.__tecnico = tecnico
        self.__salario = salario
        self.__multa_rescisoria = multa_rescisoria
        
    
    @property
    def clube(self):
        return self.__clube
    
    @clube.setter
    def clube(self, clube):
        self.__clube = clube
        
    @property
    def tecnico(self):
        return self.__tecnico
    
    @tecnico.setter
    def tecnico(self, tecnico):
        self.__tecnico = tecnico
        
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
        