from entidades.contrato_tecnico import ContratoTecnico
from excecoes.cpf_invalido_error import CpfInvalidoError
from excecoes.salario_invalido_error import SalarioInvalidoError
from excecoes.multa_rescisoria_invalida_error import MultaRescisoriaInvalidaError
from telas.tela_contrato_tecnico import TelaContratoTecnico
import streamlit as st
from entidades.tecnico import Tecnico
from entidades.contrato_tecnico import ContratoTecnico
from entidades.clube import Clube


class ControladorContratoTecnico:
    def __init__(self, controlador_clube):
        self.__controlador_clube = controlador_clube
        self.__tela_contrato = TelaContratoTecnico()
        self.__contratos = []

    def abre_tela(self):
        if not st.session_state.clube_selecionado:
            self.__tela_contrato.mostra_mensagem(
                "Selecione um clube primeiro!")
            st.session_state.tela_atual = 'clube'
            st.rerun()
            return

        opcao = self.__tela_contrato.tela_inicial_contrato_tecnico()

        if st.session_state.sub_tela == 'contratar':
            dados_contrato = self.__tela_contrato.pega_dados_contrato()
            if dados_contrato is not None:
                tecnico = self.__controlador_clube.controlador_sistema.controlador_tecnico.pega_tecnico_por_cpf(
                    dados_contrato["cpf"])
                if not tecnico:
                    self.__tela_contrato.mostra_mensagem(
                        "Técnico não encontrado!")
                    return

                if self.pega_contrato_por_tecnico(tecnico):
                    self.__tela_contrato.mostra_mensagem(
                        "Técnico já possui contrato!")
                    return

                novo_contrato = ContratoTecnico(
                    tecnico,
                    st.session_state.clube_selecionado,
                    dados_contrato["salario"],
                    dados_contrato["multa_rescisoria"]
                )
                self.__contratos.append(novo_contrato)
                st.session_state.clube_selecionado.contrato_tecnico = novo_contrato
                self.__tela_contrato.mostra_mensagem(
                    "Contrato realizado com sucesso!")

        elif st.session_state.sub_tela == 'alterar':
            cpf = self.__tela_contrato.seleciona_contrato()
            if cpf is not None:
                tecnico = self.__controlador_clube.controlador_sistema.controlador_tecnico.pega_tecnico_por_cpf(
                    cpf)
                if tecnico:
                    contrato = self.pega_contrato_por_tecnico(tecnico)
                    if contrato:
                        # Implementar lógica de alteração
                        pass
                    else:
                        self.__tela_contrato.mostra_mensagem(
                            "Contrato não encontrado!")
                else:
                    self.__tela_contrato.mostra_mensagem(
                        "Técnico não encontrado!")

        elif st.session_state.sub_tela == 'listar':
            contratos_clube = [
                c for c in self.__contratos if c.clube == st.session_state.clube_selecionado]
            self.__tela_contrato.mostra_contrato(contratos_clube)

        elif st.session_state.sub_tela == 'demitir':
            cpf = self.__tela_contrato.seleciona_contrato()
            if cpf is not None:
                tecnico = self.__controlador_clube.controlador_sistema.controlador_tecnico.pega_tecnico_por_cpf(
                    cpf)
                if tecnico:
                    contrato = self.pega_contrato_por_tecnico(tecnico)
                    if contrato:
                        if self.__tela_contrato.confirma_demissao(contrato):
                            self.__contratos.remove(contrato)
                            st.session_state.clube_selecionado.contrato_tecnico = None
                            self.__tela_contrato.mostra_mensagem(
                                "Técnico demitido com sucesso!")
                    else:
                        self.__tela_contrato.mostra_mensagem(
                            "Contrato não encontrado!")
                else:
                    self.__tela_contrato.mostra_mensagem(
                        "Técnico não encontrado!")

    def pega_contrato_por_tecnico(self, tecnico: Tecnico):
        for contrato in self.__contratos:
            if contrato.tecnico == tecnico:
                return contrato
        return None

    @property
    def contratos(self):
        return self.__contratos
