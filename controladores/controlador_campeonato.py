import streamlit as st
from telas.tela_campeonato import TelaCampeonato
from entidades.campeonato import Campeonato
from daos.dao_campeonato import CampeonatoDAO

class ControladorCampeonato:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_campeonato = TelaCampeonato()
        self.__campeonato_dao = CampeonatoDAO()
        self.__campeonatos = {campeonato.nome: campeonato for campeonato in self.__campeonato_dao.get_all()}

    def abre_tela(self):
        opcao = self.__tela_campeonato.tela_inicial_campeonato()

        if st.session_state.sub_tela == 'cadastrar':
            dados_campeonato = self.__tela_campeonato.tela_cadastro_campeonato()
            if dados_campeonato is not None:
                if dados_campeonato["nome"] in self.__campeonatos:
                    self.__tela_campeonato.mostra_mensagem("Campeonato já cadastrado!")
                else:
                    novo_campeonato = Campeonato(
                        dados_campeonato["nome"],
                        dados_campeonato["premiacao"],
                        dados_campeonato["numero_times"],
                        dados_campeonato["numero_estrangeiros"],
                        dados_campeonato["numero_jogadores"]
                    )
                    self.__campeonatos[novo_campeonato.nome] = novo_campeonato
                    self.__campeonato_dao.add(novo_campeonato)
                    self.__tela_campeonato.mostra_mensagem("Campeonato cadastrado com sucesso!")

        elif st.session_state.sub_tela == 'alterar':
            nome = self.__tela_campeonato.seleciona_campeonato()
            if nome is not None:
                campeonato = self.__campeonatos.get(nome)
                if campeonato:
                    dados_campeonato = self.__tela_campeonato.tela_cadastro_campeonato()
                    if dados_campeonato is not None:
                        campeonato.nome = dados_campeonato["nome"]
                        campeonato.premiacao = dados_campeonato["premiacao"]
                        campeonato.regra.numero_times = dados_campeonato["numero_times"]
                        campeonato.regra.numero_estrangeiros = dados_campeonato["numero_estrangeiros"]
                        campeonato.regra.numero_jogadores = dados_campeonato["numero_jogadores"]
                        self.__campeonato_dao.update(campeonato)
                        self.__tela_campeonato.mostra_mensagem("Campeonato alterado com sucesso!")
                else:
                    self.__tela_campeonato.mostra_mensagem("Campeonato não encontrado!")

        elif st.session_state.sub_tela == 'listar':
            self.__tela_campeonato.mostra_campeonato(list(self.__campeonatos.values()))

        elif st.session_state.sub_tela == 'excluir':
            nome = self.__tela_campeonato.seleciona_campeonato()
            if nome is not None:
                campeonato = self.__campeonatos.get(nome)
                if campeonato:
                    del self.__campeonatos[campeonato.nome]
                    self.__campeonato_dao.remove(campeonato.nome)
                    self.__tela_campeonato.mostra_mensagem("Campeonato excluído com sucesso!")
                else:
                    self.__tela_campeonato.mostra_mensagem("Campeonato não encontrado!")

    def pega_campeonato_por_nome(self, nome: str):
        return self.__campeonatos.get(nome)