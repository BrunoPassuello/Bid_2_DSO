from controladores.controlador_tecnico import ControladorTecnico
from telas.tela_sistema import TelaSistema

class ControladorSistema:
    def __init__(self):
        #self.__controlador_clube = ControladorClube()
        self.__controlador_tecnico = ControladorTecnico(self)
        #self.__controlador_jogador = ControladorJogador()
        #self.__controlador_campeonato = ControladorCampeonato()
        self.__tela_sistema = TelaSistema()
    
    def inicializa_sistema(self):
        self.abre_tela()

    def cadastra_clubes(self):
        # Chama o controlador de Livros
        self.__controlador_clubes.abre_tela()

    def cadastra_jogadores(self):
        # Chama o controlador de Amigos
        self.__controlador_jogadores.abre_tela()

    def cadastra_tecnicos(self):
        # Chama o controlador de Emprestimos
        self.__controlador_tecnico.abre_tela()

    def cadastra_campeonatos(self):
        # Chama o controlador de Emprestimos
        self.__controlador_campeonatos.abre_tela()

    def encerra_sistema(self):
        exit(0)

    def abre_tela(self):
        lista_opcoes = {1: self.cadastra_clubes, 
                        2: self.cadastra_jogadores, 
                        3: self.cadastra_tecnicos,
                        4: self.cadastra_campeonatos,
                        0: self.encerra_sistema}

        while True:
            opcao_escolhida = self.__tela_sistema.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()