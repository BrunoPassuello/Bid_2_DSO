import streamlit as st
from telas.tela_sistema import TelaSistema
from controladores.controlador_clube import ControladorClube
from controladores.controlador_jogador import ControladorJogador
from controladores.controlador_tecnico import ControladorTecnico
from controladores.controlador_campeonato import ControladorCampeonato


class ControladorSistema:
    def __init__(self):
        self.__tela_sistema = TelaSistema()
        self.__controlador_clube = ControladorClube(self)
        self.__controlador_jogador = ControladorJogador(self)
        self.__controlador_tecnico = ControladorTecnico(self)
        self.__controlador_campeonato = ControladorCampeonato(self)

    def inicializa_sistema(self):
        if 'tela_atual' not in st.session_state:
            st.session_state.tela_atual = 'sistema'
        if 'sub_tela' not in st.session_state:
            st.session_state.sub_tela = None

    def abre_tela(self):
        self.inicializa_sistema()

        if st.session_state.tela_atual == 'sistema':
            opcao = self.__tela_sistema.tela_opcoes()

        elif st.session_state.tela_atual == 'clube':
            self.__controlador_clube.abre_tela()

        elif st.session_state.tela_atual == 'jogador':
            self.__controlador_jogador.abre_tela()

        elif st.session_state.tela_atual == 'tecnico':
            self.__controlador_tecnico.abre_tela()

        elif st.session_state.tela_atual == 'campeonato':
            self.__controlador_campeonato.abre_tela()

    def encerra_sistema(self):
        exit(0)
