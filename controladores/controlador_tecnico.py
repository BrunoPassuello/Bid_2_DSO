import streamlit as st
from telas.tela_tecnico import TelaTecnico
from entidades.tecnico import Tecnico
from entidades.licenca import Licenca


class ControladorTecnico:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_tecnico = TelaTecnico()
        self.__tecnicos = []

    def abre_tela(self):
        opcao = self.__tela_tecnico.tela_inicial_tecnico()

        if st.session_state.sub_tela == 'cadastrar':
            dados_tecnico = self.__tela_tecnico.tela_cadastro_tecnico()
            if dados_tecnico is not None:
                if self.pega_tecnico_por_cpf(dados_tecnico["cpf"]):
                    self.__tela_tecnico.mostra_mensagem(
                        "Técnico já cadastrado!")
                else:
                    licenca = Licenca[dados_tecnico["licenca"].replace(
                        " ", "_").upper()]
                    novo_tecnico = Tecnico(
                        dados_tecnico["nome"],
                        dados_tecnico["cpf"],
                        dados_tecnico["idade"],
                        dados_tecnico["pais"],
                        licenca
                    )
                    self.__tecnicos.append(novo_tecnico)
                    self.__tela_tecnico.mostra_mensagem(
                        "Técnico cadastrado com sucesso!")

        elif st.session_state.sub_tela == 'alterar':
            cpf = self.__tela_tecnico.seleciona_tecnico()
            if cpf is not None:
                tecnico = self.pega_tecnico_por_cpf(cpf)
                if tecnico:
                    dados_atualizados = self.__tela_tecnico.pega_dados_atualizacao(
                        tecnico)
                    if dados_atualizados is not None:
                        tecnico.nome = dados_atualizados["nome"]
                        tecnico.idade = dados_atualizados["idade"]
                        tecnico.pais = dados_atualizados["pais"]
                        tecnico.licenca = Licenca[dados_atualizados["licenca"].replace(
                            " ", "_").upper()]
                        self.__tela_tecnico.mostra_mensagem(
                            "Técnico alterado com sucesso!")
                else:
                    self.__tela_tecnico.mostra_mensagem(
                        "Técnico não encontrado!")

        elif st.session_state.sub_tela == 'listar':
            self.__tela_tecnico.mostra_tecnico(self.__tecnicos)

        elif st.session_state.sub_tela == 'excluir':
            cpf = self.__tela_tecnico.seleciona_tecnico()
            if cpf is not None:
                tecnico = self.pega_tecnico_por_cpf(cpf)
                if tecnico:
                    if self.__tela_tecnico.confirma_exclusao(tecnico):
                        self.__tecnicos.remove(tecnico)
                        self.__tela_tecnico.mostra_mensagem(
                            "Técnico excluído com sucesso!")
                else:
                    self.__tela_tecnico.mostra_mensagem(
                        "Técnico não encontrado!")

    def pega_tecnico_por_cpf(self, cpf: str):
        for tecnico in self.__tecnicos:
            if tecnico.cpf == cpf:
                return tecnico
        return None

    @property
    def tecnicos(self):
        return self.__tecnicos
