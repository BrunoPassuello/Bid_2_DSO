from telas.tela_clube import TelaClube
from entidades.Clube import Clube

#bruno: lembra q o clube tem na lista "jogadores" ta os contratos,
# n os jogadores direto
class ControladorClube:
    def __init__(self, controlador_sistema):
        self.__tela_clube = TelaClube()
        self.__controlador_principal = controlador_sistema
        self.__clubes = []
        self.__clube_selecionado = None
    def abre_tela_clube(self):
        lista_opcoes = {
            1: self.seleciona_clube,
            2: self.cadastrar_clube,
            3: self.alterar_clube,
            4: self.listar_clubes,
            5: self.excluir_clube,
            0: self.retornar
        }
        continua = True
        while continua:
            lista_opcoes[self.__tela_clube.tela_inicial_clube()]()
    def clube_selecionado(self):
        clube = self.__tela_clube.seleciona_clube()
        self.__clube_selecionado = clube
        while True:
            valor_lido = self.__tela_clube.mostra_opcoes()
            funcao_escolhida = lista_opcoes[valor_lido]
            funcao_escolhida()
    def seleciona_clube(self):
        nome_clube = self.__tela_clube.seleciona_clube()
        for clube in self.__clubes:
            if clube.nome == nome_clube:
                self.__tela_clube.mostra_clube(clube)
                break
        else:
            self.__tela_clube.clube_nao_cadastrado()
    def cadastrar_clube(self):
        nome_clube = self.__tela_clube.cadastra_clube()
        clube = Clube(nome_clube)
        self.__clubes.append(clube)

    def listar_clubes(self):
        self.__tela_clube.mostra_clubes(self.__clubes)

    def retornar(self):
        self.__clube_selecionado = None
        self.__controlador_principal.abre_tela_principal()
#Não deixar Controlador Sistema de fora
#Controlador Contrato para contratar jogadores
#Posição faz sentido existir?
#Cidade faz sentido existir?
#Tela clube jogador vai virar tela de contrato jogador sem  a opção de listar jogadores
#Tela clube tecnico vai virar tela de contrato tecnico sem a opção de listar tecnicos