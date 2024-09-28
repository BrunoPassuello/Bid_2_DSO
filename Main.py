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

#instanciando pais, estado e cidade
Brasil = Pais("Brasil")
Sao_Paulo_Es = Estado("São Paulo Estado", Brasil)
Sao_Paulo_Ci = Cidade("São Paulo Cidade", Sao_Paulo_Es)

#instanciando posição
atacante = Posicao("Atacante")

#instanciando jogador
jogador = Jogador("Neymar", 29, Sao_Paulo_Ci, atacante, 1.75, 68, True)

#instanciando clube
santos = Clube("Santos", Sao_Paulo_Ci)
palmeiras = Clube("Palmeiras", Sao_Paulo_Ci)

#contrato de jogador
santos.contratar_jogador(jogador, 1000000, 10000000, True)

#jogador com maior salario e jogador com maior multa
print(santos.jogador_maior_salario())
print(santos.jogador_maior_multa())
pele = Jogador("Pelé", 80, Sao_Paulo_Ci, atacante, 1.75, 68, True)
santos.contratar_jogador(pele, 100000000000, 1000000000000, True)
print(santos.jogador_maior_salario())
print(santos.jogador_maior_multa())

#Listar jogadores
santos.listar_jogadores()

print("----------------------------------------------------------------")

#Método informaçoes_jogador
santos.informacoes_jogador(jogador)

print("----------------------------------------------------------------")

#demitir jogador
santos.demitir_jogador(pele)
santos.listar_jogadores()

#teste de cidade, estado e pais de um jogador
print(jogador.cidade.estado.pais.nome)
print(jogador.cidade.estado.nome)
print(jogador.cidade.nome)

print("----------------------------------------------------------------")

#teste de cidade, estado e pais de um clube
print(santos.cidade.estado.pais.nome)
print(santos.cidade.estado.nome)
print(santos.cidade.nome)

print("----------------------------------------------------------------")

#criação do tecnico
licenca = Licenca("Licença A")
tecnico = Tecnico("Tite", 59, Sao_Paulo_Ci, licenca)

#contrato de tecnico
santos.contratar_tecnico(tecnico, 5000, 10000)
print(santos.contrato_tecnico.tecnico.nome)

print("----------------------------------------------------------------")

#criação de campeonato, clube entrar no campeonato, listar clubes em campeonato
brasileirao = Campeonato("Brasileirão", 2021, 20, 5, 22)

#clube entrar no campeonato
santos.entrar_campeonato(brasileirao)
palmeiras.entrar_campeonato(brasileirao)

#listar clubes em campeonato
brasileirao.listar_clubes()

#clube sair do campeonato
santos.sair_campeonato(brasileirao)
brasileirao.listar_clubes()

#tecnico do clube
print(santos.tecnico())

print("----------------------------------------------------------------")

santos.listar_contrato_tecnico()

print("----------------------------------------------------------------")

santos.demitir_tecnico()
santos.tecnico()



