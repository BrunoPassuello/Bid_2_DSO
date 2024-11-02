from controladores.controlador_contrato_jogador import ControladorContratoJogador
from controladores.controlador_tecnico import ControladorTecnico
from controladores.controlador_jogador import ControladorJogador
from telas.tela_sistema import TelaSistema

class ControladorSistema:
    def __init__(self):
        # Inicialização dos controladores
        self.__controlador_tecnico = ControladorTecnico(self)
        self.__controlador_jogador = ControladorJogador(self)
        self.__controlador_contrato_jogador = ControladorContratoJogador(self)
        self.__tela_sistema = TelaSistema()
    
    def cadastra_contratos(self):
        self.__controlador_contrato_jogador.abre_tela()

    def abre_tela(self):
        lista_opcoes = {
            1: self.cadastra_clubes, 
            2: self.cadastra_jogadores, 
            3: self.cadastra_tecnicos,
            4: self.cadastra_campeonatos,
            5: self.cadastra_contratos,
            0: self.encerra_sistema
        }

        while True:
            opcao = self.__tela_sistema.tela_opcoes()
            funcao_escolhida = lista_opcoes.get(opcao)
            if funcao_escolhida:
                funcao_escolhida()
            else:
                self.__tela_sistema.mostra_mensagem("Opção inválida.")
