import streamlit as st
from entidades.clube import Clube
from entidades.tecnico import Tecnico
from entidades.jogador import Jogador
from entidades.contrato_jogador import ContratoJogador
from entidades.contrato_tecnico import ContratoTecnico
from telas.tela_clube import TelaClube
from telas.tela_contrato_jogador import TelaContratoJogador
from telas.tela_contrato_tecnico import TelaContratoTecnico
from daos.dao_clube import ClubeDAO

class ControladorClube:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_clube = TelaClube()
        self.__clube_dao = ClubeDAO()
        self.__clubes = {clube.id: clube for clube in self.__clube_dao.get_all()}
        self.__clube_selecionado = None
        self.__controlador_contrato_jogador = None
        self.__controlador_contrato_tecnico = None

    def abre_tela(self):
        opcao = self.__tela_clube.tela_inicial_clube()

        if st.session_state.sub_tela == 'selecionar':
            nome = self.__tela_clube.seleciona_clube()
            if nome is not None:
                clube = self.pega_clube_por_nome(nome)
                if clube:
                    st.session_state.clube_selecionado = clube
                    st.session_state.sub_tela = 'clube_selecionado'
                    st.rerun()
                else:
                    self.__tela_clube.clube_nao_cadastrado()

        elif st.session_state.sub_tela == 'clube_selecionado':
            opcao = self.__tela_clube.tela_clube_selecionado()
            if opcao == 1:  # Jogadores
                if self.__controlador_contrato_jogador is None:
                    from controladores.controlador_contrato_jogador import ControladorContratoJogador
                    self.__controlador_contrato_jogador = ControladorContratoJogador(self)
                st.session_state.tela_atual = 'contrato_jogador'
                st.rerun()
            elif opcao == 2:  # Técnico
                if self.__controlador_contrato_tecnico is None:
                    from controladores.controlador_contrato_tecnico import ControladorContratoTecnico
                    self.__controlador_contrato_tecnico = ControladorContratoTecnico(self)
                st.session_state.tela_atual = 'contrato_tecnico'
                st.rerun()
            elif opcao == 3:  # Campeonatos
                self.gerenciar_campeonatos()
            elif opcao == 4:  # Informações
                self.mostrar_informacoes_clube()

        elif st.session_state.sub_tela == 'cadastrar':
            dados_clube = self.__tela_clube.tela_cadastra_clube()
            if dados_clube is not None:
                if self.pega_clube_por_nome(dados_clube["nome"]):
                    self.__tela_clube.mostra_mensagem("Clube já cadastrado!")
                else:
                    novo_clube = Clube(dados_clube["nome"], dados_clube["pais"])
                    self.__clubes[novo_clube.id] = novo_clube
                    self.__clube_dao.add(novo_clube)
                    self.__tela_clube.mostra_mensagem("Clube cadastrado com sucesso!")

        elif st.session_state.sub_tela == 'alterar':
            nome = self.__tela_clube.seleciona_clube()
            if nome is not None:
                clube = self.pega_clube_por_nome(nome)
                if clube:
                    dados_clube = self.__tela_clube.tela_cadastra_clube()
                    if dados_clube is not None:
                        clube.nome = dados_clube["nome"]
                        clube.pais = dados_clube["pais"]
                        self.__clube_dao.update(clube)
                        self.__tela_clube.mostra_mensagem("Clube alterado com sucesso!")
                else:
                    self.__tela_clube.clube_nao_cadastrado()

        elif st.session_state.sub_tela == 'listar':
            self.__tela_clube.mostra_clube(list(self.__clubes.values()))

        elif st.session_state.sub_tela == 'excluir':
            nome = self.__tela_clube.seleciona_clube()
            if nome is not None:
                clube = self.pega_clube_por_nome(nome)
                if clube:
                    del self.__clubes[clube.id]
                    self.__clube_dao.remove(clube.id)
                    self.__tela_clube.mostra_mensagem("Clube excluído com sucesso!")
                else:
                    self.__tela_clube.clube_nao_cadastrado()

    def pega_clube_por_nome(self, nome: str):
        for clube in self.__clubes.values():
            if clube.nome == nome:
                return clube
        return None

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
        jogador = max(self.__clube_selecionado.jogadores, key=lambda j: j.salario)
        self.__tela_clube.mostra_mensagem(f"Jogador com maior salário: {jogador.nome} - R${jogador.salario}")

    def jogador_menor_salario(self):
        jogador = min(self.__clube_selecionado.jogadores, key=lambda j: j.salario)
        self.__tela_clube.mostra_mensagem(f"Jogador com menor salário: {jogador.nome} - R${jogador.salario}")

    def jogador_maior_multa(self):
        jogador = max(self.__clube_selecionado.jogadores, key=lambda j: j.multa_rescisoria)
        self.__tela_clube.mostra_mensagem(f"Jogador com maior multa rescisória: {jogador.nome} - R${jogador.multa_rescisoria}")

    def jogador_menor_multa(self):
        jogador = min(self.__clube_selecionado.jogadores, key=lambda j: j.multa_rescisoria)
        self.__tela_clube.mostra_mensagem(f"Jogador com menor multa rescisória: {jogador.nome} - R${jogador.multa_rescisoria}")

    def gerenciar_campeonatos(self):
        opcoes = {
            1: self.participar_campeonato,
            2: self.sair_campeonato,
            3: self.listar_campeonatos,
            4: self.campeonato_maior_premiacao,
            0: self.retornar_menu_principal
        }

        while True:
            opcao = self.__tela_clube.tela_gerenciar_campeonatos()
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
            self.__tela_clube.mostra_mensagem("Clube inscrito no campeonato com sucesso!")
        else:
            self.__tela_clube.mostra_mensagem("Campeonato não encontrado!")

    def sair_campeonato(self):
        nome_campeonato = self.__tela_clube.seleciona_campeonato()
        campeonato = next((c for c in self.__clube_selecionado.campeonatos if c.nome == nome_campeonato), None)
        if campeonato:
            self.__clube_selecionado.campeonatos.remove(campeonato)
            self.__tela_clube.mostra_mensagem("Clube removido do campeonato com sucesso!")
        else:
            self.__tela_clube.mostra_mensagem("Campeonato não encontrado!")

    def listar_campeonatos(self):
        if self.__clube_selecionado:
            self.__tela_clube.mostra_campeonatos(self.__clube_selecionado.campeonatos)
        else:
            self.__tela_clube.mostra_mensagem("Nenhum clube selecionado.")

    def campeonato_maior_premiacao(self):
        if not self.__clube_selecionado.campeonatos:
            self.__tela_clube.mostra_mensagem("O clube não está em nenhum campeonato.")
            return
        campeonato = max(self.__clube_selecionado.campeonatos, key=lambda c: c.premiacao)
        self.__tela_clube.mostra_mensagem(f"Campeonato com maior premiação: {campeonato.nome} - R${campeonato.premiacao}")

    def retornar_menu_principal(self):
        st.session_state.tela_atual = 'sistema'
        st.session_state.sub_tela = None
        st.rerun()

    def retornar_menu_clube_selecionado(self):
        st.session_state.sub_tela = 'clube_selecionado'
        st.rerun()

    @property
    def clube_selecionado(self):
        return self.__clube_selecionado

    @clube_selecionado.setter
    def clube_selecionado(self, clube):
        self.__clube_selecionado = clube

    @property
    def clubes(self):
        return self.__clubes