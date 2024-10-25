from telas.tela_jogador import TelaJogador
from entidades.Jogador import Jogador

class ControladorJogador:
    def __init__(self, controlador_sistema):
        self.__jogadores = []
        self.__tela_jogador = TelaJogador()
        self.__controlador_sistema = controlador_sistema
            
    def pega_jogador_por_cpf(self, cpf):
        for jogador in self.__jogadores:
            if jogador.cpf == cpf:
                return jogador
        return None

    def incluir_jogador(self):
        dados_jogador = self.__tela_jogador.tela_cadastro_jogador()
        # to convertendo para booleano ao incluir dados do jogador
        dados_jogador["estrangeiro"] = True if dados_jogador["estrangeiro"].upper() == "S" else False
        
        jogador = Jogador(
            dados_jogador["nome"], 
            dados_jogador["cpf"],
            dados_jogador["idade"],
            dados_jogador["cidade"],
            dados_jogador["posicao"],
            dados_jogador["peso"],
            dados_jogador["altura"],
            dados_jogador["estrangeiro"])
        self.__jogadores.append(jogador)

    def alterar_jogador(self):
        self.listar_jogador()
        cpf = self.__tela_jogador.seleciona_jogador()
        jogador = self.pega_jogador_por_cpf(cpf)
        if jogador is not None:
            dados_jogador = self.__tela_jogador.tela_cadastro_jogador()
            # conversão deve estar aqui também(caso de naturalização)
            dados_jogador["estrangeiro"] = True if dados_jogador["estrangeiro"].upper() == "S" else False
            
            jogador.nome = dados_jogador["nome"]
            jogador.idade = dados_jogador["idade"]
            jogador.cidade = dados_jogador["cidade"]
            jogador.posicao = dados_jogador["posicao"]
            jogador.peso = dados_jogador["peso"]
            jogador.altura = dados_jogador["altura"]
            jogador.estrangeiro = dados_jogador["estrangeiro"]
        else:
            print("ATENÇÃO: Jogador não encontrado!")

    def excluir_jogador(self):
        self.listar_jogador()
        cpf = self.__tela_jogador.seleciona_jogador()
        jogador = self.pega_jogador_por_cpf(cpf)
        if jogador is not None:
            self.__jogadores.remove(jogador)
        else:
            print("ATENÇÃO: Jogador não encontrado!")

    def listar_jogador(self):
        self.__tela_jogador.mostra_jogador(self.__jogadores)

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {
            1: self.incluir_jogador,
            2: self.alterar_jogador,
            3: self.listar_jogador,
            4: self.excluir_jogador,
            0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_jogador.tela_inicial_jogador()]()