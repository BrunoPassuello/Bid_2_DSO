from controladores.controlador_contrato_jogador import ControladorContratoJogador
from controladores.controlador_tecnico import ControladorTecnico
from controladores.controlador_jogador import ControladorJogador
from telas.tela_sistema import TelaSistema

class ControladorSistema:
    def __init__(self):
        self.__controlador_tecnico = ControladorTecnico(self)
        self.__controlador_jogador = ControladorJogador(self)
        self.__controlador_contrato_jogador = ControladorContratoJogador(self)
        self.__tela_sistema = TelaSistema()

    def inicializa_sistema(self):
        """Método para iniciar o sistema e abrir a tela principal."""
        self.abre_tela()  

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
            # Exibe a tela de opções e obtém a escolha do usuário
            opcao = self.__tela_sistema.tela_opcoes()
            funcao_escolhida = lista_opcoes.get(opcao)

            if funcao_escolhida:
                funcao_escolhida()  # Chama a função correspondente
            else:
                self.__tela_sistema.mostra_mensagem("Opção inválida.")
