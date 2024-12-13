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

                try:
                    # Create new contract
                    novo_contrato = ContratoJogador(
                        clube=st.session_state.clube_selecionado,
                        jogador=jogador,
                        salario=dados_contrato["salario"],
                        multa_rescisoria=dados_contrato["multa_rescisoria"],
                        contrato_produtividade=dados_contrato["contrato_produtividade"]
                    )

                    # Add contract to club's list
                    st.session_state.clube_selecionado.jogadores.append(
                        novo_contrato)

                    # Update club in DAO
                    self.__controlador_clube._ControladorClube__clube_dao.update(
                        st.session_state.clube_selecionado)

                    self.__tela_contrato.mostra_mensagem(
                        "Contrato criado com sucesso!")
                    st.session_state.sub_tela = None
                    st.rerun()

                except Exception as e:
                    self.__tela_contrato.mostra_mensagem(str(e))
                    return

        elif st.session_state.sub_tela == 'listar':
            if st.session_state.clube_selecionado.jogadores:
                for contrato in st.session_state.clube_selecionado.jogadores:
                    self.__tela_contrato.mostra_contrato(contrato)
            else:
                self.__tela_contrato.mostra_mensagem(
                    "Não há jogadores contratados!")

        elif st.session_state.sub_tela == 'demitir':
            cpf = self.__tela_contrato.seleciona_contrato()
            if cpf is not None:
                contrato = None
                for contrato_jogador in st.session_state.clube_selecionado.jogadores:
                    if contrato_jogador.jogador.cpf == int(cpf):
                        contrato = contrato_jogador
                        break

                if contrato:
                    confirmacao = self.__tela_contrato.confirma_demissao(contrato)
                    if confirmacao is True:
                        try:
                            # 1. Pega referências necessárias
                            jogador = contrato.jogador
                            clube = st.session_state.clube_selecionado
                            
                            # 2. Remove jogador do clube
                            if clube.remover_jogador(contrato):
                                # 3. Atualiza o jogador no DAO
                                self.__controlador_clube.controlador_sistema.controlador_jogador.jogador_dao.update(jogador)
                                
                                # 4. Atualiza o clube no DAO
                                self.__controlador_clube._ControladorClube__clube_dao.update(clube)
                                
                                # 5. Atualiza a sessão
                                st.session_state.clube_selecionado = clube
                                
                                # 6. Mostra mensagem de sucesso e retorna
                                self.__tela_contrato.mostra_mensagem("Jogador demitido com sucesso!")
                                st.session_state.sub_tela = None
                                st.rerun()
                            else:
                                self.__tela_contrato.mostra_mensagem("Erro ao remover jogador do clube!")
                        except Exception as e:
                            self.__tela_contrato.mostra_mensagem(f"Erro ao demitir jogador: {str(e)}")
                else:
                    self.__tela_contrato.mostra_mensagem("Jogador não encontrado no clube!")

    def pega_contrato_por_jogador(self, jogador: Jogador):
        for contrato in self.__contratos:
            if contrato.jogador == jogador:
                return contrato
        return None
