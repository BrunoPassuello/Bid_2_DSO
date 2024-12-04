from daos.dao import DAO
from entidades.tecnico import Tecnico

#cada entidade terá uma classe dessa, implementação bem simples.
class TecnicoDAO(DAO):
    def __init__(self):
        super().__init__('tecnicos.pkl')

    def add(self, tecnico : Tecnico):
        if((tecnico is not None) and isinstance(tecnico, Tecnico) and isinstance(tecnico.cpf, int)):
            super().add(tecnico.cpf, tecnico)

    def update(self, tecnico: Tecnico):
        if((tecnico is not None) and isinstance(tecnico, Tecnico) and isinstance(tecnico.cpf, int)):
            super().update(tecnico.cpf, tecnico)

    def get(self, key:int):
        if isinstance(key, int):
            return super().get(key)

    def remove(selfself, key:int):
        if(isinstance(key, int)):
            return super().remove(key)