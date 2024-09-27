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
from Campeonato import Campeonato

Brasil = Pais("Brasil")
Sao_Paulo_Es = Estado("São Paulo Estado", Brasil)
Sao_Paulo_Ci = Cidade("São Paulo Cidade", Sao_Paulo_Es)

atacante = Posicao("Atacante")

jogador = Jogador("Neymar", 29, Sao_Paulo_Ci, atacante, 1.75, 68, True)
santos = Clube("Santos", Sao_Paulo_Ci)
palmeiras = Clube("Palmeiras", Sao_Paulo_Ci)
santos.contratar_jogador(jogador, 1000000, 10000000, True)
print(jogador.cidade.estado.pais.nome)
print(jogador.cidade.estado.nome)
print(jogador.cidade.nome)
print("----------------------------------------------------------------")

print(santos.cidade.estado.pais.nome)
print(santos.cidade.estado.nome)
print(santos.cidade.nome)
print("----------------------------------------------------------------")

licenca = Licenca("Licença A")
tecnico = Tecnico("Tite", 59, Sao_Paulo_Ci, licenca)

santos.contratar_tecnico(tecnico, 5000, 10000)
print(santos.contrato_tecnico.tecnico.nome)
print("----------------------------------------------------------------")
brasileirao = Campeonato("Brasileirão", 2021, 20, 5, 22)
santos.entrar_campeonato(brasileirao)
palmeiras.entrar_campeonato(brasileirao)
brasileirao.listar_clubes()
print("----------------------------------------------------------------")
santos.sair_campeonato(brasileirao)
brasileirao.listar_clubes()
print(santos.tecnico())
