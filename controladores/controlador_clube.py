from entidades.clube import Clube
from entidades.tecnico import Tecnico
from entidades.jogador import Jogador
from entidades.contrato_jogador import ContratoJogador
from entidades.contrato_tecnico import ContratoTecnico
from telas.tela_clube import TelaClube
from telas.tela_contrato_jogador import TelaContratoJogador
from telas.tela_contrato_tecnico import TelaContratoTecnico

class ControladorClube:
    def __init__(self, controlador_sistema):
        self.__clubes = [] 
        self.__clube_selecionado = None  
        self.__tela_clube = TelaClube()
        self.__controlador_sistema = controlador_sistema

    def cadastrar_clube(self):
        dados_clube = self.__tela_clube.tela_cadastra_clube()
        clube = Clube(dados_clube["nome"], dados_clube["País"])
        self.__clubes.append(clube)
        self.__tela_clube.mostra_mensagem("Clube cadastrado com sucesso!")

    def selecionar_clube(self):
        nome_clube = self.__tela_clube.seleciona_clube()
        clube = next((c for c in self.__clubes if c.nome == nome_clube), None)
        
        if clube:
            self.__clube_selecionado = clube
            self.__tela_clube.mostra_mensagem("Clube selecionado com sucesso!")
            self.tela_clube_selecionado()
        else:
            self.__tela_clube.clube_nao_cadastrado()

    def listar_clubes(self):
        self.__tela_clube.mostra_clube(self.__clubes)

    def alterar_clube(self):
        nome_clube = self.__tela_clube.seleciona_clube()
        clube = next((c for c in self.__clubes if c.nome == nome_clube), None)
        
        if clube:
            dados = self.__tela_clube.tela_cadastra_clube()
            clube.nome = dados["nome"]
            clube.pais = dados["País"]
            self.__tela_clube.mostra_mensagem("Informações do clube alteradas com sucesso.")
        else:
            self.__tela_clube.clube_nao_cadastrado()

    def excluir_clube(self):
        nome_clube = self.__tela_clube.seleciona_clube()
        clube = next((c for c in self.__clubes if c.nome == nome_clube), None)
        
        if clube:
            self.__clubes.remove(clube)
            self.__tela_clube.mostra_mensagem("Clube excluído com sucesso!")
        else:
            self.__tela_clube.clube_nao_cadastrado()

    def tela_clube_selecionado(self):
        if not self.__clube_selecionado:
            self.__tela_clube.mostra_mensagem("Nenhum clube selecionado!")
            return
        
        opcoes = {
            1: self.gerenciar_jogadores,
            2: self.gerenciar_tecnico,
            3: self.gerenciar_campeonatos,
            4: self.mostrar_informacoes_clube,
            0: self.retornar_menu_principal
        }

        while True:
            opcao = self.__tela_clube.tela_clube_selecionado()
            acao = opcoes.get(opcao)
            if acao:
                acao()
            else:
                self.__tela_clube.mostra_mensagem("Opção inválida.")

    def gerenciar_jogadores(self):
        opcao = self.__tela_clube.tela_clube_jogador()
        if opcao == 1:
            self.__tela_clube.mostra_clube(self.__clube_selecionado.jogadores)
        elif opcao == 2:
            self.__controlador_sistema.controlador_contrato_jogador.abre_tela()
        elif opcao == 0:
            self.retornar_menu_clube_selecionado()

    def gerenciar_tecnico(self):
        opcao = self.__tela_clube.tela_clube_tecnico()
        if opcao == 1:
            if self.__clube_selecionado.contrato_tecnico:
                self.__tela_clube.mostra_mensagem("Técnico: " + self.__clube_selecionado.contrato_tecnico.tecnico.nome)
            else:
                self.__tela_clube.mostra_mensagem("O clube não possui técnico.")
        elif opcao == 2:
            self.__controlador_sistema.controlador_contrato_tecnico.abre_tela()
        elif opcao == 0:
            self.retornar_menu_clube_selecionado()

    def gerenciar_campeonatos(self):
        opcoes = {
            1: self.participar_campeonato,
            2: self.sair_campeonato,
            3: self.listar_campeonatos,
            4: self.campeonato_maior_premiacao,
            0: self.retornar_menu_clube_selecionado
        }

        while True:
            opcao = self.__tela_clube.tela_clube_campeonato()
            acao = opcoes.get(opcao)
            if acao:
                acao()
            else:
                self.__tela_clube.mostra_mensagem("Opção inválida.")

    def participar_campeonato(self):
        nome_campeonato = self.__tela_clube.seleciona_campeonato()
        campeonato = self.__controlador_sistema.controlador_campeonato.pega_campeonato_por_nome(nome_campeonato)
        if campeonato:
            self.__clube_selecionado.campeonatos.append(campeonato)
            self.__tela_clube.mostra_mensagem("Clube adicionado ao campeonato.")
        else:
            self.__tela_clube.mostra_mensagem("Campeonato não encontrado.")

    def sair_campeonato(self):
        nome_campeonato = self.__tela_clube.seleciona_campeonato()
        campeonato = next((c for c in self.__clube_selecionado.campeonatos if c.nome == nome_campeonato), None)
        if campeonato:
            self.__clube_selecionado.campeonatos.remove(campeonato)
            self.__tela_clube.mostra_mensagem("Clube saiu do campeonato.")
        else:
            self.__tela_clube.mostra_mensagem("Campeonato não encontrado.")

    def listar_campeonatos(self):
        self.__tela_clube.mostra_campeonatos(self.__clube_selecionado.campeonatos)

    def campeonato_maior_premiacao(self):
        if not self.__clube_selecionado.campeonatos:
            self.__tela_clube.mostra_mensagem("O clube não está em nenhum campeonato.")
            return
        campeonato = max(self.__clube_selecionado.campeonatos, key=lambda c: c.premiacao)
        self.__tela_clube.mostra_mensagem(f"Campeonato com maior premiação: {campeonato.nome} - R${campeonato.premiacao}")

    def mostrar_informacoes_clube(self):
        opcoes = {
            1: self.relatorio_clube,
            2: self.jogador_maior_salario,
            3: self.jogador_menor_salario,
            4: self.jogador_maior_multa,
            5: self.jogador_menor_multa,
            0: self.retornar_menu_clube_selecionado
        }

        while True:
            opcao = self.__tela_clube.tela_clube_informacoes()
            acao = opcoes.get(opcao)
            if acao:
                acao()
            else:
                self.__tela_clube.mostra_mensagem("Opção inválida.")

    def relatorio_clube(self):
        self.__tela_clube.relatorio_clube(
            self.__clube_selecionado,
            self.__clube_selecionado.jogadores,
            self.__clube_selecionado.campeonatos
        )

    def jogador_maior_salario(self):
        maior_salario_jogador = max(self.__clube_selecionado.jogadores, key=lambda c: c.salario, default=None)
        if maior_salario_jogador:
            self.__tela_clube.relatorio_maior_salario(maior_salario_jogador.jogador)
        else:
            self.__tela_clube.mostra_mensagem("Nenhum jogador encontrado.")

    def jogador_menor_salario(self):
        menor_salario_jogador = min(self.__clube_selecionado.jogadores, key=lambda c: c.salario, default=None)
        if menor_salario_jogador:
            self.__tela_clube.relatorio_menor_salario(menor_salario_jogador.jogador)
        else:
            self.__tela_clube.mostra_mensagem("Nenhum jogador encontrado.")

    def jogador_maior_multa(self):
        maior_multa_jogador = max(self.__clube_selecionado.jogadores, key=lambda c: c.multa_rescisoria, default=None)
        if maior_multa_jogador:
            self.__tela_clube.relatorio_maior_multa(maior_multa_jogador.jogador)
        else:
            self.__tela_clube.mostra_mensagem("Nenhum jogador encontrado.")

    def jogador_menor_multa(self):
        menor_multa_jogador = min(self.__clube_selecionado.jogadores, key=lambda c: c.multa_rescisoria, default=None)
        if menor_multa_jogador:
            self.__tela_clube.relatorio_menor_multa(menor_multa_jogador.jogador)
        else:
            self.__tela_clube.mostra_mensagem("Nenhum jogador encontrado.")

    def retornar_menu_clube_selecionado(self):
        self.tela_clube_selecionado()

    def retornar_menu_principal(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        opcoes = {
            1: self.selecionar_clube,
            2: self.cadastrar_clube,
            3: self.alterar_clube,
            4: self.listar_clubes,
            5: self.excluir_clube,
            0: self.retornar_menu_principal
        }

        while True:
            opcao = self.__tela_clube.tela_inicial_clube()
            acao = opcoes.get(opcao)
            if acao:
                acao()
            else:
                self.__tela_clube.mostra_mensagem("Opção inválida.")