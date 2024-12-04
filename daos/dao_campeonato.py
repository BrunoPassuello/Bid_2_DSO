from daos.dao import DAO
from entidades.campeonato import Campeonato

#cada entidade terá uma classe dessa, implementação bem simples.
class CampeonatoDAO(DAO):
    def __init__(self):
        super().__init__('campeonatos.pkl')

    def add(self, campeonato: Campeonato):
        if((campeonato is not None) and isinstance(campeonato, Campeonato) and isinstance(campeonato.nome, int)):
            super().add(campeonato.nome, campeonato)

    def update(self, campeonato: Campeonato):
        if((campeonato is not None) and isinstance(campeonato, Campeonato) and isinstance(campeonato.nome, int)):
            super().update(campeonato.nome, campeonato)

    def get(self, key: int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key: int):
        if(isinstance(key, int)):
            return super().remove(key)