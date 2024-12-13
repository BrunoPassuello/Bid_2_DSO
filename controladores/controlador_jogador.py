from telas.tela_jogador import TelaJogador
from entidades.jogador import Jogador
from entidades.posicao import Posicao
from daos.dao_jogador import JogadorDAO
import streamlit as st


class ControladorJogador:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_jogador = TelaJogador()
        self.__jogador_DAO = JogadorDAO()

    def abre_tela(self):
        opcao = self.__tela_jogador.tela_inicial_jogador()

        if opcao == 1:
            st.session_state.sub_tela = 'cadastrar'
        elif opcao == 2:
            st.session_state.sub_tela = 'listar'
        elif opcao == 3:
            st.session_state.sub_tela = 'excluir'
        elif opcao == 0:
            st.session_state.tela_atual = 'sistema'
            st.session_state.sub_tela = None
            st.rerun()
            return

        if st.session_state.sub_tela == 'cadastrar':
            self.incluir_jogador()
        elif st.session_state.sub_tela == 'listar':
            self.listar_jogador()
        elif st.session_state.sub_tela == 'excluir':
            self.excluir_jogador()

    def pega_jogador_por_cpf(self, cpf):
        try:
            return self.__jogador_DAO.get(int(cpf))
        except:
            return None

    def incluir_jogador(self):
        dados_jogador = self.__tela_jogador.tela_cadastro_jogador()
        if dados_jogador is not None:
            if self.pega_jogador_por_cpf(dados_jogador["cpf"]):
                self.__tela_jogador.mostra_mensagem("Jogador já cadastrado!")
            else:
                posicao = Posicao(dados_jogador["posicao"])
                novo_jogador = Jogador(
                    dados_jogador["nome"],
                    int(dados_jogador["cpf"]),
                    dados_jogador["idade"],
                    dados_jogador["pais"],
                    posicao,
                    dados_jogador["peso"],
                    dados_jogador["altura"],
                    dados_jogador["estrangeiro"] == "S"
                )
                self.__jogador_DAO.add(novo_jogador)
                self.__tela_jogador.mostra_mensagem("Jogador cadastrado com sucesso!")

    def excluir_jogador(self):
        cpf = self.__tela_jogador.seleciona_jogador()
        if cpf is not None:
            jogador = self.pega_jogador_por_cpf(cpf)
            if jogador:
                self.__jogador_DAO.remove(int(cpf))
                self.__tela_jogador.mostra_mensagem("Jogador excluído com sucesso!")
            else:
                self.__tela_jogador.mostra_mensagem("Jogador não encontrado!")

    def listar_jogador(self):
        self.__tela_jogador.mostra_mensagem("Jogadores Cadastrados:")
        for jogador in self.__jogador_DAO.get_all():
            self.__tela_jogador.mostra_jogador(jogador)

    def retornar(self):
        self.__controlador_sistema.abre_tela()
