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
        self.__controlador_contrato_jogador = None
        self.__controlador_contrato_tecnico = None
        self.__clube_selecionado = None

    def abre_tela(self):
        opcao = self.__tela_clube.tela_inicial_clube()

        if st.session_state.sub_tela == 'selecionar':
            nome = self.__tela_clube.seleciona_clube()
            if nome is not None:
                clube = self.pega_clube_por_nome(nome)
                if clube:
                    self.__clube_selecionado = clube
                    st.session_state.clube_selecionado = clube
                    st.session_state.sub_tela = 'clube_selecionado'
                    st.rerun()
                else:
                    self.__tela_clube.mostra_mensagem("Clube não cadastrado!")

        elif st.session_state.sub_tela == 'clube_selecionado':
            opcao = self.__tela_clube.tela_clube_selecionado()
            if opcao == 1:  # Jogadores
                if self.__controlador_contrato_jogador is None:
                    from controladores.controlador_contrato_jogador import ControladorContratoJogador
                    self.__controlador_contrato_jogador = ControladorContratoJogador(self)
                st.session_state.tela_atual = 'contrato_jogador'
                st.session_state.sub_tela = None
                st.rerun()
                return
            elif opcao == 2:  # Técnico
                if self.__controlador_contrato_tecnico is None:
                    from controladores.controlador_contrato_tecnico import ControladorContratoTecnico
                    self.__controlador_contrato_tecnico = ControladorContratoTecnico(self)
                st.session_state.tela_atual = 'contrato_tecnico'
                st.session_state.sub_tela = None
                st.rerun()
                return
            elif opcao == 3:  # Campeonatos
                st.session_state.tela_atual = 'campeonato'
                st.session_state.sub_tela = None
                st.rerun()
                return
            elif opcao == 4:  # Informações
                st.session_state.sub_tela = 'informacoes'
                st.rerun()
                return
            elif opcao == 0:  # Retornar
                st.session_state.sub_tela = None
                if hasattr(st.session_state, 'clube_selecionado'):
                    del st.session_state.clube_selecionado
                st.rerun()

        elif st.session_state.sub_tela == 'cadastrar':
            dados_clube = self.__tela_clube.tela_cadastra_clube()
            if dados_clube is not None:
                if self.pega_clube_por_nome(dados_clube["nome"]):
                    self.__tela_clube.mostra_mensagem("Clube já cadastrado!")
                else:
                    novo_clube = Clube(dados_clube["nome"], dados_clube["pais"])
                    self.__clube_dao.add(novo_clube)
                    self.__tela_clube.mostra_mensagem("Clube cadastrado com sucesso!")

        elif st.session_state.sub_tela == 'listar':
            self.__tela_clube.mostra_mensagem("Clubes Cadastrados:")
            for clube in self.__clube_dao.get_all():
                self.__tela_clube.mostra_clube(clube)

        elif st.session_state.sub_tela == 'excluir':
            nome = self.__tela_clube.seleciona_clube()
            if nome is not None:
                clube = self.pega_clube_por_nome(nome)
                if clube:
                    self.__clube_dao.remove(clube.id)
                    self.__tela_clube.mostra_mensagem("Clube excluído com sucesso!")
                else:
                    self.__tela_clube.mostra_mensagem("Clube não cadastrado!")

        elif st.session_state.sub_tela == 'informacoes':
            self.mostrar_informacoes_clube()
            if hasattr(st.session_state, 'relatorio_tipo'):
                if st.session_state.relatorio_tipo == "maior_salario":
                    self.jogador_maior_salario()
                elif st.session_state.relatorio_tipo == "menor_salario":
                    self.jogador_menor_salario()
                elif st.session_state.relatorio_tipo == "maior_multa":
                    self.jogador_maior_multa()
                elif st.session_state.relatorio_tipo == "menor_multa":
                    self.jogador_menor_multa()
                # Clear the report type after showing the result
                del st.session_state.relatorio_tipo

    @property
    def controlador_sistema(self):
        return self.__controlador_sistema

    def pega_clube_por_nome(self, nome: str):
        clubes = self.__clube_dao.get_all()
        for clube in clubes:
            if clube.nome.lower() == nome.lower():
                return clube
        return None

    def mostrar_informacoes_clube(self):
        self.__tela_clube.tela_clube_informacoes()

    def relatorio_clube(self):
        self.__tela_clube.relatorio_clube(
            self.__clube_selecionado,
            self.__clube_selecionado.jogadores,
            self.__clube_selecionado.campeonatos
        )

    def jogador_maior_salario(self):
        if not self.__clube_selecionado:
            self.__tela_clube.mostra_mensagem("Nenhum clube selecionado!")
            return
        if not self.__clube_selecionado.jogadores:
            self.__tela_clube.mostra_mensagem("O clube não possui jogadores!")
            return
        try:
            jogador = max(self.__clube_selecionado.jogadores, key=lambda j: j.salario)
            self.__tela_clube.mostra_mensagem(
                f"Jogador com maior salário: {jogador.jogador.nome} - R${jogador.salario:,.2f}")
        except Exception as e:
            self.__tela_clube.mostra_mensagem(f"Erro ao buscar jogador: {str(e)}")

    def jogador_menor_salario(self):
        if not self.__clube_selecionado:
            self.__tela_clube.mostra_mensagem("Nenhum clube selecionado!")
            return
        if not self.__clube_selecionado.jogadores:
            self.__tela_clube.mostra_mensagem("O clube não possui jogadores!")
            return
        try:
            jogador = min(self.__clube_selecionado.jogadores, key=lambda j: j.salario)
            self.__tela_clube.mostra_mensagem(
                f"Jogador com menor salário: {jogador.jogador.nome} - R${jogador.salario:,.2f}")
        except Exception as e:
            self.__tela_clube.mostra_mensagem(f"Erro ao buscar jogador: {str(e)}")

    def jogador_maior_multa(self):
        if not self.__clube_selecionado:
            self.__tela_clube.mostra_mensagem("Nenhum clube selecionado!")
            return
        if not self.__clube_selecionado.jogadores:
            self.__tela_clube.mostra_mensagem("O clube não possui jogadores!")
            return
        try:
            jogador = max(self.__clube_selecionado.jogadores, key=lambda j: j.multa_rescisoria)
            self.__tela_clube.mostra_mensagem(
                f"Jogador com maior multa rescisória: {jogador.jogador.nome} - R${jogador.multa_rescisoria:,.2f}")
        except Exception as e:
            self.__tela_clube.mostra_mensagem(f"Erro ao buscar jogador: {str(e)}")

    def jogador_menor_multa(self):
        if not self.__clube_selecionado:
            self.__tela_clube.mostra_mensagem("Nenhum clube selecionado!")
            return
        if not self.__clube_selecionado.jogadores:
            self.__tela_clube.mostra_mensagem("O clube não possui jogadores!")
            return
        try:
            jogador = min(self.__clube_selecionado.jogadores, key=lambda j: j.multa_rescisoria)
            self.__tela_clube.mostra_mensagem(
                f"Jogador com menor multa rescisória: {jogador.jogador.nome} - R${jogador.multa_rescisoria:,.2f}")
        except Exception as e:
            self.__tela_clube.mostra_mensagem(f"Erro ao buscar jogador: {str(e)}")

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