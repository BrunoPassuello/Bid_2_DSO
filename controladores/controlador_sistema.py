from controladores.controlador_clube import ControladorClube
from controladores.controlador_contrato_jogador import ControladorContratoJogador
from controladores.controlador_tecnico import ControladorTecnico
from controladores.controlador_jogador import ControladorJogador
from controladores.controlador_campeonato import ControladorCampeonato
from telas.tela_sistema import TelaSistema

class ControladorSistema:
    def __init__(self):
        self.__controlador_clube = ControladorClube(self)
        self.__controlador_contrato_jogador = ControladorContratoJogador(self)
        self.__controlador_tecnico = ControladorTecnico(self)
        self.__controlador_jogador = ControladorJogador(self)
        self.__controlador_campeonato = ControladorCampeonato(self)
        self.__tela_sistema = TelaSistema()

    @property
    def controlador_clube(self):
        return self.__controlador_clube

    @property
    def controlador_contrato_jogador(self):
        return self.__controlador_contrato_jogador

    @property
    def controlador_tecnico(self):
        return self.__controlador_tecnico

    @property
    def controlador_jogador(self):
        return self.__controlador_jogador

    @property
    def controlador_campeonato(self):
        return self.__controlador_campeonato

    def inicializa_sistema(self):
        """Método para iniciar o sistema e abrir a tela principal."""
        self.abre_tela()

    def abre_tela(self):
        lista_opcoes = {
            1: self.__controlador_clube.abre_tela,
            2: self.__controlador_jogador.abre_tela,
            3: self.__controlador_tecnico.abre_tela,
            4: self.__controlador_campeonato.abre_tela,
            0: self.encerra_sistema
        }

        while True:
            opcao = self.__tela_sistema.tela_opcoes()
            funcao_escolhida = lista_opcoes.get(opcao)
            if funcao_escolhida:
                funcao_escolhida()
            else:
                self.__tela_sistema.mostra_mensagem("Opção inválida.")

    def encerra_sistema(self):
        exit(0)
