from daos.dao import DAO
from entidades.jogador import Jogador


class JogadorDAO(DAO):
    def __init__(self):
        super().__init__('jogadores.pkl')

    def add(self, jogador: Jogador):
        if((jogador is not None) and isinstance(jogador, Jogador) and isinstance(jogador.cpf, int)):
            super().add(jogador.cpf, jogador)

    def update(self, jogador: Jogador):
        if((jogador is not None) and isinstance(jogador, Jogador) and isinstance(jogador.cpf, int)):
            super().update(jogador.cpf, jogador)

    def get(self, key: int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key: int):
        if(isinstance(key, int)):
            return super().remove(key)