import streamlit as st
from telas.tela_campeonato import TelaCampeonato
from entidades.campeonato import Campeonato
from entidades.regra import Regra


class ControladorCampeonato:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_campeonato = TelaCampeonato()
        self.__campeonatos = []

    def abre_tela(self):
        opcao = self.__tela_campeonato.tela_inicial_campeonato()

        if st.session_state.sub_tela == 'cadastrar':
            dados_campeonato = self.__tela_campeonato.tela_cadastro_campeonato()
            if dados_campeonato is not None:
                # Lógica de cadastro
                pass

        elif st.session_state.sub_tela == 'alterar':
            nome = self.__tela_campeonato.seleciona_campeonato()
            if nome is not None:
                # Lógica de alteração
                pass

        elif st.session_state.sub_tela == 'listar':
            self.__tela_campeonato.mostra_campeonato(self.__campeonatos)

        elif st.session_state.sub_tela == 'excluir':
            nome = self.__tela_campeonato.seleciona_campeonato()
            if nome is not None:
                # Lógica de exclusão
                pass
