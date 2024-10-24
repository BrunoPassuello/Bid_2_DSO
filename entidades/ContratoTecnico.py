from entidades.Clube import Clube
from entidades.Tecnico import Tecnico
from entidades.Contrato import Contrato

class ContratoTecnico(Contrato):
    def __init__(self, clube : Clube, tecnico : Tecnico, salario : float, multa_rescisoria : float):
        super().__init__(clube, salario, multa_rescisoria)
        self.__tecnico = tecnico
        
    @property
    def tecnico(self):
        return self.__tecnico
    
    @tecnico.setter
    def tecnico(self, tecnico):
        self.__tecnico = tecnico