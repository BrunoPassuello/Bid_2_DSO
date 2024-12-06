from excecoes.cpf_invalido_error import CpfInvalidoError
from excecoes.salario_invalido_error import SalarioInvalidoError
from excecoes.multa_rescisoria_invalida_error import MultaRescisoriaInvalidaError
from entidades.contrato_jogador import ContratoJogador
from telas.tela_contrato_jogador import TelaContratoJogador
import streamlit as st
from entidades.jogador import Jogador


class ControladorContratoJogador:
    def __init__(self, controlador_clube):
        self.__controlador_clube = controlador_clube
        self.__tela_contrato = TelaContratoJogador()
        self.__contratos = []

    def abre_tela(self):
        if not st.session_state.clube_selecionado:
            self.__tela_contrato.mostra_mensagem(
                "Selecione um clube primeiro!")
            st.session_state.tela_atual = 'clube'
            st.rerun()
            return

        opcao = self.__tela_contrato.tela_inicial_contrato_jogador()

        if st.session_state.sub_tela == 'contratar':
            dados_contrato = self.__tela_contrato.pega_dados_contrato()
            if dados_contrato is not None:
                jogador = self.__controlador_clube.controlador_sistema.controlador_jogador.pega_jogador_por_cpf(
                    dados_contrato["cpf"])
                if not jogador:
                    self.__tela_contrato.mostra_mensagem(
                        "Jogador não encontrado!")
                    return

                if self.pega_contrato_por_jogador(jogador):
                    self.__tela_contrato.mostra_mensagem(
                        "Jogador já possui contrato!")
                    return

    def pega_contrato_por_jogador(self, jogador: Jogador):
        for contrato in self.__contratos:
            if contrato.jogador == jogador:
                return contrato
        return None
