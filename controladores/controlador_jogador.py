import streamlit as st
from telas.tela_jogador import TelaJogador
from entidades.jogador import Jogador
from entidades.posicao import Posicao


class ControladorJogador:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_jogador = TelaJogador()
        self.__jogadores = []

    def abre_tela(self):
        opcao = self.__tela_jogador.tela_inicial_jogador()

        if st.session_state.sub_tela == 'cadastrar':
            dados_jogador = self.__tela_jogador.tela_cadastro_jogador()
            if dados_jogador is not None:
                if self.pega_jogador_por_cpf(dados_jogador["cpf"]):
                    self.__tela_jogador.mostra_mensagem(
                        "Jogador já cadastrado!")
                else:
                    posicao = Posicao[dados_jogador["posicao"].upper()]
                    novo_jogador = Jogador(
                        dados_jogador["nome"],
                        dados_jogador["cpf"],
                        dados_jogador["idade"],
                        dados_jogador["pais"],
                        posicao,
                        dados_jogador["peso"],
                        dados_jogador["altura"],
                        dados_jogador["estrangeiro"] == "S"
                    )
                    self.__jogadores.append(novo_jogador)
                    self.__tela_jogador.mostra_mensagem(
                        "Jogador cadastrado com sucesso!")

        elif st.session_state.sub_tela == 'alterar':
            cpf = self.__tela_jogador.seleciona_jogador()
            if cpf is not None:
                jogador = self.pega_jogador_por_cpf(cpf)
                if jogador:
                    dados_atualizados = self.__tela_jogador.pega_dados_atualizacao(
                        jogador)
                    if dados_atualizados is not None:
                        jogador.nome = dados_atualizados["nome"]
                        jogador.idade = dados_atualizados["idade"]
                        jogador.pais = dados_atualizados["pais"]
                        jogador.posicao = Posicao[dados_atualizados["posicao"].upper(
                        )]
                        jogador.peso = dados_atualizados["peso"]
                        jogador.altura = dados_atualizados["altura"]
                        jogador.estrangeiro = dados_atualizados["estrangeiro"] == "S"
                        self.__tela_jogador.mostra_mensagem(
                            "Jogador alterado com sucesso!")
                else:
                    self.__tela_jogador.mostra_mensagem(
                        "Jogador não encontrado!")

        elif st.session_state.sub_tela == 'listar':
            self.__tela_jogador.mostra_jogador(self.__jogadores)

        elif st.session_state.sub_tela == 'excluir':
            cpf = self.__tela_jogador.seleciona_jogador()
            if cpf is not None:
                jogador = self.pega_jogador_por_cpf(cpf)
                if jogador:
                    if self.__tela_jogador.confirma_exclusao(jogador):
                        self.__jogadores.remove(jogador)
                        self.__tela_jogador.mostra_mensagem(
                            "Jogador excluído com sucesso!")
                else:
                    self.__tela_jogador.mostra_mensagem(
                        "Jogador não encontrado!")

    def pega_jogador_por_cpf(self, cpf):
        for jogador in self.__jogadores:
            if jogador.cpf == cpf:
                return jogador
        return None

    def incluir_jogador(self):
        dados_jogador = self.__tela_jogador.tela_cadastro_jogador()
        dados_jogador["estrangeiro"] = True if dados_jogador["estrangeiro"].upper(
        ) == "S" else False

        jogador = Jogador(
            dados_jogador["nome"],
            dados_jogador["cpf"],
            dados_jogador["idade"],
            dados_jogador["pais"],
            dados_jogador["posicao"],
            dados_jogador["peso"],
            dados_jogador["altura"],
            dados_jogador["estrangeiro"]
        )
        self.__jogadores.append(jogador)
        self.__tela_jogador.mostra_mensagem("Jogador cadastrado com sucesso!")

        jogador_cadastrado = self.pega_jogador_por_cpf(jogador.cpf)
        if jogador_cadastrado:
            self.__tela_jogador.mostra_mensagem(
                "Jogador encontrado após o cadastro.")
        else:
            self.__tela_jogador.mostra_mensagem(
                "Jogador não encontrado após o cadastro.")
        return jogador

    def alterar_jogador(self):
        self.listar_jogador()
        cpf = self.__tela_jogador.seleciona_jogador()
        jogador = self.pega_jogador_por_cpf(cpf)
        if jogador is not None:
            dados_jogador = self.__tela_jogador.tela_cadastro_jogador()
            # conversão deve estar aqui também(caso de naturalização)
            dados_jogador["estrangeiro"] = True if dados_jogador["estrangeiro"].upper(
            ) == "S" else False

            jogador.nome = dados_jogador["nome"]
            jogador.idade = dados_jogador["idade"]
            jogador.pais = dados_jogador["pais"]
            jogador.posicao = Posicao(dados_jogador["posicao"])
            jogador.peso = dados_jogador["peso"]
            jogador.altura = dados_jogador["altura"]
            jogador.estrangeiro = dados_jogador["estrangeiro"]
        else:
            self.__tela_jogador.mostra_mensagem(
                "ATENÇÃO: Jogador não encontrado!")

    def excluir_jogador(self):
        self.listar_jogador()
        cpf = self.__tela_jogador.seleciona_jogador()
        jogador = self.pega_jogador_por_cpf(cpf)
        if jogador is not None:
            self.__jogadores.remove(jogador)
        else:
            self.__tela_jogador.mostra_mensagem(
                "ATENÇÃO: Jogador não encontrado!")

    def listar_jogador(self):
        self.__tela_jogador.mostra_jogador(self.__jogadores)

    def retornar(self):
        self.__controlador_sistema.abre_tela()
