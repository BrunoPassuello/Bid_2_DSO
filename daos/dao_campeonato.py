from daos.dao import DAO
from entidades.campeonato import Campeonato

class CampeonatoDAO(DAO):
    def __init__(self):
        super().__init__('campeonatos.pkl')

    def add(self, campeonato: Campeonato):
        if campeonato is not None and isinstance(campeonato, Campeonato):
            super().add(campeonato.nome, campeonato)

    def update(self, campeonato: Campeonato):
        if campeonato is not None and isinstance(campeonato, Campeonato):
            super().update(campeonato.nome, campeonato)

    def get(self, key: str):
        if isinstance(key, str):
            return super().get(key)

    def remove(self, key: str):
        if isinstance(key, str):
            return super().remove(key)