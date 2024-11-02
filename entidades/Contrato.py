from entidades.clube import Clube
class Contrato:
    def __init__(self, clube : Clube, salario : float, multa_rescisoria : float):
        self.clube = clube
        self.salario = salario
        self.multa_rescisoria = multa_rescisoria
    
    @property
    def clube(self):
        return self._clube
    
    @clube.setter
    def clube(self, clube):
        self._clube = clube

    @property
    def salario(self):
        return self._salario
    
    @salario.setter
    def salario(self, salario):
        self._salario = salario

    @property
    def multa_rescisoria(self):
        return self._multa_rescisoria
    
    @multa_rescisoria.setter
    def multa_rescisoria(self, multa_rescisoria):
        self._multa_rescisoria = multa_rescisoria
    