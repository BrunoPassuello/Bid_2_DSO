from daos.dao import DAO
from entidades.clube import Clube

#cada entidade terá uma classe dessa, implementação bem simples.
class ClubeDAO(DAO):
    def __init__(self):
        super().__init__('clubes.pkl')

    def add(self, clube: Clube):
        if((clube is not None) and isinstance(clube, Clube) and isinstance(clube.id, int)):
            super().add(clube.id, clube)

    def update(self, clube: Clube):
        if((clube is not None) and isinstance(clube, Clube) and isinstance(clube.id, int)):
            super().update(clube.id, clube)

    def get(self, key: int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key: int):
        if(isinstance(key, int)):
            return super().remove(key)