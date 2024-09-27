from clube import Clube
from Jogador import Jogador
from ContratoJogador import ContratoJogador
jogador = Jogador("Neymar", 29, "Atacante", 1.75, 68.5, False)
clube = Clube("Paris Saint-Germain")
clube.contratar_jogador(jogador, 1000000, 10000000, True)
