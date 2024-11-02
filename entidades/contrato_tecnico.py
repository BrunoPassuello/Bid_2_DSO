from entidades.clube import Clube
from entidades.tecnico import Tecnico
from entidades.contrato import Contrato

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