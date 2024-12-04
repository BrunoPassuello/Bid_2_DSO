import streamlit as st
from telas.tela_clube import TelaClube
from entidades.clube import Clube
from controladores.controlador_contrato_jogador import ControladorContratoJogador
from controladores.controlador_contrato_tecnico import ControladorContratoTecnico


class ControladorClube:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_clube = TelaClube()
        self.__clubes = []
        self.__controlador_contrato_jogador = ControladorContratoJogador(self)
        self.__controlador_contrato_tecnico = ControladorContratoTecnico(self)

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
                st.session_state.tela_atual = 'contrato_jogador'
                st.rerun()
            elif opcao == 2:  # Técnico
                st.session_state.tela_atual = 'contrato_tecnico'
                st.rerun()
            elif opcao == 3:  # Campeonatos
                # Implementar lógica de campeonatos
                pass
            elif opcao == 4:  # Informações
                self.mostra_informacoes_clube()

        elif st.session_state.sub_tela == 'cadastrar':
            dados_clube = self.__tela_clube.tela_cadastra_clube()
            if dados_clube is not None:
                if self.pega_clube_por_nome(dados_clube["nome"]):
                    self.__tela_clube.mostra_mensagem("Clube já cadastrado!")
                else:
                    novo_clube = Clube(
                        dados_clube["nome"], dados_clube["pais"])
                    self.__clubes.append(novo_clube)
                    self.__tela_clube.mostra_mensagem(
                        "Clube cadastrado com sucesso!")

        elif st.session_state.sub_tela == 'alterar':
            nome = self.__tela_clube.seleciona_clube()
            if nome is not None:
                clube = self.pega_clube_por_nome(nome)
                if clube:
                    # Implementar lógica de alteração
                    pass
                else:
                    self.__tela_clube.clube_nao_cadastrado()

        elif st.session_state.sub_tela == 'listar':
            self.__tela_clube.mostra_clube(self.__clubes)

        elif st.session_state.sub_tela == 'excluir':
            nome = self.__tela_clube.seleciona_clube()
            if nome is not None:
                clube = self.pega_clube_por_nome(nome)
                if clube:
                    self.__clubes.remove(clube)
                    self.__tela_clube.mostra_mensagem(
                        "Clube excluído com sucesso!")
                else:
                    self.__tela_clube.clube_nao_cadastrado()

    # ... outros métodos permanecem iguais ...

    @property
    def clube_selecionado(self):
        return self.__clube_selecionado
