from Licenca import Licenca
from Pais import Pais
from Estado import Estado
from Cidade import Cidade
from Clube import Clube
from Jogador import Jogador
from ContratoJogador import ContratoJogador
from Pais import Pais
from Posicao import Posicao
from Tecnico import Tecnico

Brasil = Pais("Brasil")
Sao_Paulo_Es = Estado("São Paulo Estado", Brasil)
Sao_Paulo_Ci = Cidade("São Paulo Cidade", Sao_Paulo_Es)

atacante = Posicao("Atacante")

jogador = Jogador("Neymar", 29, Sao_Paulo_Ci, atacante, 1.75, 68, True)
clube = Clube("Santos", Sao_Paulo_Ci)
clube.contratar_jogador(jogador, 1000000, 10000000, True)
print(jogador.cidade.estado.pais.nome)
print(jogador.cidade.estado.nome)
print(jogador.cidade.nome)

print(clube.cidade.estado.pais.nome)
print(clube.cidade.estado.nome)
print(clube.cidade.nome)

licenca = Licenca("Licença A")
tecnico = Tecnico("Tite", 59, Sao_Paulo_Ci, licenca)