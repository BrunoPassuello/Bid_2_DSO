from daos.dao_tecnico import TecnicoDAO
import streamlit as st
from telas.tela_tecnico import TelaTecnico
from entidades.tecnico import Tecnico
from entidades.licenca import Licenca
from excecoes.cpf_invalido_error import CpfInvalidoError
from excecoes.salario_invalido_error import SalarioInvalidoError
from excecoes.multa_rescisoria_invalida_error import MultaRescisoriaInvalidaError
from entidades.contrato_jogador import ContratoJogador
from telas.tela_contrato_jogador import TelaContratoJogador
from entidades.jogador import Jogador
from entidades.contrato_tecnico import ContratoTecnico
from telas.tela_contrato_tecnico import TelaContratoTecnico
from entidades.clube import Clube


class ControladorTecnico:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_tecnico = TelaTecnico()
        self.__tecnico_DAO = TecnicoDAO()

    def abre_tela(self):
        opcao = self.__tela_tecnico.tela_inicial_tecnico()

        if st.session_state.sub_tela == 'cadastrar':
            dados_tecnico = self.__tela_tecnico.tela_cadastro_tecnico()
            if dados_tecnico is not None:
                if self.pega_tecnico_por_cpf(dados_tecnico["cpf"]):
                    self.__tela_tecnico.mostra_mensagem(
                        "Técnico já cadastrado!")
                else:
                    licenca = Licenca(dados_tecnico["licenca"])
                    novo_tecnico = Tecnico(
                        dados_tecnico["nome"],
                        int(dados_tecnico["cpf"]),
                        dados_tecnico["idade"],
                        dados_tecnico["pais"],
                        licenca
                    )
                    try:
                        self.__tecnico_DAO.add(novo_tecnico)
                        self.__tela_tecnico.mostra_mensagem(
                            "Técnico cadastrado com sucesso!")
                    except (CpfInvalidoError, SalarioInvalidoError, MultaRescisoriaInvalidaError) as e:
                        self.__tela_tecnico.mostra_mensagem(str(e))

        elif st.session_state.sub_tela == 'listar':
            tecnicos = self.__tecnico_DAO.get_all()
            self.__tela_tecnico.mostra_tecnicos(tecnicos)

        elif st.session_state.sub_tela == 'excluir':
            cpf = self.__tela_tecnico.seleciona_tecnico()
            if cpf is not None:
                tecnico = self.pega_tecnico_por_cpf(int(cpf))
                if tecnico:
                    if self.__tela_tecnico.confirma_exclusao(tecnico):
                        self.__tecnico_DAO.remove(tecnico.cpf)
                        self.__tela_tecnico.mostra_mensagem(
                            "Técnico excluído com sucesso!")
                        st.session_state.sub_tela = 'listar'
                else:
                    self.__tela_tecnico.mostra_mensagem(
                        "Técnico não encontrado!")

    def pega_tecnico_por_cpf(self, cpf: int):
        try:
            return self.__tecnico_DAO.get(cpf)
        except ChaveInvalidaError:
            return None

    @property
    def tecnicos(self):
        return self.__tecnico_DAO.get_all()
