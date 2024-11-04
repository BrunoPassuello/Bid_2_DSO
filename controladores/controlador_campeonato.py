from entidades.campeonato import Campeonato
from telas.tela_campeonato import TelaCampeonato
from excecoes.nome_clube_invalido_error import NomeClubeInvalidoError

class ControladorCampeonato:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__campeonatos = []
        self.__tela_campeonato = TelaCampeonato()

    def cadastrar_campeonato(self):
        dados_campeonato = self.__tela_campeonato.tela_cadastro_campeonato()
        if dados_campeonato is None:
            return
        try:
            premiacao = float(dados_campeonato["premiacao"])
            numero_times = int(dados_campeonato["numero_times"])
            numero_estrangeiros = int(dados_campeonato["numero_estrangeiros"])
            numero_jogadores = int(dados_campeonato["numero_jogadores"])

            campeonato = Campeonato(
                nome=dados_campeonato["nome"],
                premiacao=premiacao,
                numero_times=numero_times,
                numero_estrangeiros=numero_estrangeiros,
                numero_jogadores=numero_jogadores
            )
            self.__campeonatos.append(campeonato)
            self.__tela_campeonato.mostra_mensagem("Campeonato cadastrado com sucesso!")
        except ValueError:
            self.__tela_campeonato.mostra_mensagem("Erro: Verifique os valores inseridos para premiação, número de times, estrangeiros e jogadores.")

    def alterar_campeonato(self):
        nome_campeonato = self.__tela_campeonato.seleciona_campeonato()
        campeonato = self.pega_campeonato_por_nome(nome_campeonato)

        if campeonato:
            dados_campeonato = self.__tela_campeonato.tela_cadastro_campeonato()
            try:
                campeonato.nome = dados_campeonato["nome"]
                campeonato.premiacao = float(dados_campeonato["premiacao"])
                campeonato.numero_times = int(dados_campeonato["numero_times"])
                campeonato.numero_estrangeiros = int(dados_campeonato["numero_estrangeiros"])
                campeonato.numero_jogadores = int(dados_campeonato["numero_jogadores"])
                self.__tela_campeonato.mostra_mensagem("Campeonato alterado com sucesso!")
            except ValueError:
                self.__tela_campeonato.mostra_mensagem("Erro: Verifique os valores inseridos para premiação, número de times, estrangeiros e jogadores.")
        else:
            self.__tela_campeonato.mostra_mensagem("Campeonato não encontrado.")

    def excluir_campeonato(self):
        nome_campeonato = self.__tela_campeonato.seleciona_campeonato()
        campeonato = self.pega_campeonato_por_nome(nome_campeonato)

        if campeonato:
            self.__campeonatos.remove(campeonato)
            self.__tela_campeonato.mostra_mensagem("Campeonato excluído com sucesso!")
        else:
            self.__tela_campeonato.mostra_mensagem("Campeonato não encontrado.")

    def listar_campeonatos(self):
        if not self.__campeonatos:
            self.__tela_campeonato.mostra_mensagem("Não há campeonatos cadastrados.")
        else:
            self.__tela_campeonato.mostra_campeonato(self.__campeonatos)

    def pega_campeonato_por_nome(self, nome_campeonato):
        """Retorna o campeonato que possui o nome especificado ou None se não for encontrado."""
        return next((c for c in self.__campeonatos if c.nome == nome_campeonato), None)

    def abre_tela(self):
        opcoes = {
            1: self.cadastrar_campeonato,
            2: self.alterar_campeonato,
            3: self.listar_campeonatos,
            4: self.excluir_campeonato,
            0: self.__controlador_sistema.abre_tela
        }

        while True:
            opcao = self.__tela_campeonato.tela_inicial_campeonato()
            acao = opcoes.get(opcao)
            if acao:
                acao()
            else:
                self.__tela_campeonato.mostra_mensagem("Opção inválida.")
