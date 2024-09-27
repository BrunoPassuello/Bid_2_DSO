from Pais import Pais
from Estado import Estado
from Cidade import Cidade
from Clube import Clube
from Jogador import Jogador
from ContratoJogador import ContratoJogador
from Pais import Pais

Brasil = Pais("Brasil")
Sao_Paulo_Es = Estado("São Paulo Estado", Brasil)
Sao_Paulo_Ci = Cidade("São Paulo Cidade", Sao_Paulo_Es)

jogador = Jogador("Neymar", 29, Sao_Paulo_Ci, "Atacante", 1.75, 68, True)
clube = Clube("Santos", Sao_Paulo_Ci)
clube.contratar_jogador(jogador, 1000000, 10000000, True)
print(jogador.cidade.estado.pais.nome)
print(jogador.cidade.estado.nome)
print(jogador.cidade.nome)

print(clube.cidade.estado.pais.nome)
print(clube.cidade.estado.nome)
print(clube.cidade.nome)