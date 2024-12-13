import streamlit as st
from telas.tela_sistema import TelaSistema
from controladores.controlador_jogador import ControladorJogador
from controladores.controlador_tecnico import ControladorTecnico
from controladores.controlador_campeonato import ControladorCampeonato


class ControladorSistema:
    def __init__(self):
        self.__tela_sistema = TelaSistema()
        self.__controlador_clube = None
        self.__controlador_jogador = ControladorJogador(self)
        self.__controlador_tecnico = ControladorTecnico(self)
        self.__controlador_campeonato = ControladorCampeonato(self)
        self.__controlador_contrato_jogador = None
        self.__controlador_contrato_tecnico = None

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
            if self.__controlador_clube is None:
                from controladores.controlador_clube import ControladorClube
                self.__controlador_clube = ControladorClube(self)
            self.__controlador_clube.abre_tela()

        elif st.session_state.tela_atual == 'contrato_jogador':
            if self.__controlador_contrato_jogador is None:
                from controladores.controlador_contrato_jogador import ControladorContratoJogador
                self.__controlador_contrato_jogador = ControladorContratoJogador(self.__controlador_clube)
            self.__controlador_contrato_jogador.abre_tela()

        elif st.session_state.tela_atual == 'contrato_tecnico':
            if self.__controlador_contrato_tecnico is None:
                from controladores.controlador_contrato_tecnico import ControladorContratoTecnico
                self.__controlador_contrato_tecnico = ControladorContratoTecnico(self.__controlador_clube)
            self.__controlador_contrato_tecnico.abre_tela()

        elif st.session_state.tela_atual == 'jogador':
            self.__controlador_jogador.abre_tela()

        elif st.session_state.tela_atual == 'tecnico':
            self.__controlador_tecnico.abre_tela()

        elif st.session_state.tela_atual == 'campeonato':
            self.__controlador_campeonato.abre_tela()

    @property
    def controlador_clube(self):
        return self.__controlador_clube

    @property
    def controlador_jogador(self):
        return self.__controlador_jogador

    @property
    def controlador_tecnico(self):
        return self.__controlador_tecnico

    @property
    def controlador_campeonato(self):
        return self.__controlador_campeonato

    def encerra_sistema(self):
        exit(0)