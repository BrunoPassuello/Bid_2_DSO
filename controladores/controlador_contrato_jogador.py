from excecoes.cpf_invalido_error import CpfInvalidoError
from excecoes.salario_invalido_error import SalarioInvalidoError
from excecoes.multa_rescisoria_invalida_error import MultaRescisoriaInvalidaError
from entidades.contrato_jogador import ContratoJogador
from telas.tela_contrato_jogador import TelaContratoJogador
import streamlit as st


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

                # Verifica limite de jogadores estrangeiros
                if jogador.estrangeiro:
                    contratos_clube = [
                        c for c in self.__contratos if c.clube == st.session_state.clube_selecionado]
                    estrangeiros = len(
                        [c for c in contratos_clube if c.jogador.estrangeiro])
                    if estrangeiros >= 5:  # limite de estrangeiros
                        self.__tela_contrato.mostra_mensagem(
                            "Limite de jogadores estrangeiros atingido!")
                        return

                novo_contrato = ContratoJogador(
                    jogador,
                    st.session_state.clube_selecionado,
                    dados_contrato["salario"],
                    dados_contrato["multa_rescisoria"],
                    dados_contrato["contrato_produtividade"]
                )
                self.__contratos.append(novo_contrato)
                self.__tela_contrato.mostra_mensagem(
                    "Contrato realizado com sucesso!")

        elif st.session_state.sub_tela == 'alterar':
            cpf = self.__tela_contrato.seleciona_contrato()
            if cpf is not None:
                jogador = self.__controlador_clube.controlador_sistema.controlador_jogador.pega_jogador_por_cpf(
                    cpf)
                if jogador:
                    contrato = self.pega_contrato_por_jogador(jogador)
                    if contrato:
                        dados_atualizados = self.__tela_contrato.pega_dados_atualizacao(
                            contrato)
                        if dados_atualizados is not None:
                            contrato.salario = dados_atualizados["salario"]
                            contrato.multa_rescisoria = dados_atualizados["multa_rescisoria"]
                            contrato.contrato_produtividade = dados_atualizados["contrato_produtividade"]
                            self.__tela_contrato.mostra_mensagem(
                                "Contrato alterado com sucesso!")
                    else:
                        self.__tela_contrato.mostra_mensagem(
                            "Contrato não encontrado!")
                else:
                    self.__tela_contrato.mostra_mensagem(
                        "Jogador não encontrado!")

        elif st.session_state.sub_tela == 'listar':
            contratos_clube = [
                c for c in self.__contratos if c.clube == st.session_state.clube_selecionado]
            self.__tela_contrato.mostra_contrato(contratos_clube)

        elif st.session_state.sub_tela == 'demitir':
            cpf = self.__tela_contrato.seleciona_contrato()
            if cpf is not None:
                jogador = self.__controlador_clube.controlador_sistema.controlador_jogador.pega_jogador_por_cpf(
                    cpf)
                if jogador:
                    contrato = self.pega_contrato_por_jogador(jogador)
                    if contrato:
                        if self.__tela_contrato.confirma_demissao(contrato):
                            self.__contratos.remove(contrato)
                            self.__tela_contrato.mostra_mensagem(
                                "Jogador demitido com sucesso!")
                    else:
                        self.__tela_contrato.mostra_mensagem(
                            "Contrato não encontrado!")
                else:
                    self.__tela_contrato.mostra_mensagem(
                        "Jogador não encontrado!")

    def pega_contrato_por_jogador(self, jogador: Jogador):
        for contrato in self.__contratos:
            if contrato.jogador == jogador:
                return contrato
        return None

    @property
    def contratos(self):
        return self.__contratos
