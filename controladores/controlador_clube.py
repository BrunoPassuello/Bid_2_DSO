from entidades.clube import Clube
from entidades.tecnico import Tecnico
from entidades.jogador import Jogador
from entidades.contrato_jogador import ContratoJogador
from entidades.contrato_tecnico import ContratoTecnico
from telas.tela_clube import TelaClube

class ControladorClube:
    def __init__(self, controlador_sistema):
        self.__clubes = [] 
        self.__clube_selecionado = None  
        self.__tela_clube = TelaClube()
        self.__controlador_sistema = controlador_sistema

    def cadastrar_clube(self):
        dados_clube = self.__tela_clube.tela_cadastra_clube()
        clube = Clube(dados_clube["nome"], dados_clube["cidade"])
        self.__clubes.append(clube)
        self.__tela_clube.mostra_mensagem("Clube cadastrado com sucesso!")

    def selecionar_clube(self):
        nome_clube = self.__tela_clube.seleciona_clube()
        clube = next((c for c in self.__clubes if c.nome == nome_clube), None)
        
        if clube:
            self.__clube_selecionado = clube
            self.__tela_clube.mostra_mensagem("Clube selecionado com sucesso!")
            self.tela_clube_selecionado()
        else:
            self.__tela_clube.clube_nao_cadastrado()

    def listar_clubes(self):
        self.__tela_clube.mostra_clube(self.__clubes)

    def alterar_clube(self):
        if not self.__clube_selecionado:
            self.__tela_clube.mostra_mensagem("Nenhum clube selecionado!")
            return
        
        dados = self.__tela_clube.tela_cadastra_clube()
        self.__clube_selecionado.nome = dados["nome"]
        self.__clube_selecionado.pais = dados["cidade"]
        self.__tela_clube.mostra_mensagem("Informações do clube alteradas com sucesso.")

    def excluir_clube(self):
        nome_clube = self.__tela_clube.seleciona_clube()
        clube = next((c for c in self.__clubes if c.nome == nome_clube), None)
        
        if clube:
            self.__clubes.remove(clube)
            self.__tela_clube.mostra_mensagem("Clube excluído com sucesso!")
        else:
            self.__tela_clube.clube_nao_cadastrado()

    # Métodos para operar com o clube selecionado
    def tela_clube_selecionado(self):
        if not self.__clube_selecionado:
            self.__tela_clube.mostra_mensagem("Nenhum clube selecionado!")
            return
        
        opcoes = {
            1: self.gerenciar_jogadores,
            2: self.gerenciar_tecnico,
            3: self.gerenciar_campeonatos,
            4: self.mostrar_informacoes_clube,
            0: self.retornar_menu_principal
        }

        while True:
            opcao = self.__tela_clube.tela_clube_selecionado()
            acao = opcoes.get(opcao)
            if acao:
                acao()
            else:
                self.__tela_clube.mostra_mensagem("Opção inválida.")

    def gerenciar_jogadores(self):
        # Lógica para gerenciar jogadores (contratação, demissão, listagem)
        pass

    def gerenciar_tecnico(self):
        # Lógica para gerenciar o técnico (contratação, demissão, relatórios)
        pass

    def gerenciar_campeonatos(self):
        # Lógica para gerenciar campeonatos (entrada, saída, listagem)
        pass

    # Método de exibição das informações detalhadas do clube
    def mostrar_informacoes_clube(self):
        if not self.__clube_selecionado:
            self.__tela_clube.mostra_mensagem("Nenhum clube selecionado!")
            return
        
        opcoes = {
            1: self.relatorio_clube,
            2: self.jogador_maior_salario,
            3: self.jogador_menor_salario,
            4: self.jogador_maior_multa,
            5: self.jogador_menor_multa,
            0: self.retornar_menu_clube_selecionado
        }
        
        while True:
            opcao = self.__tela_clube.tela_clube_informacoes()
            acao = opcoes.get(opcao)
            if acao:
                acao()
            else:
                self.__tela_clube.mostra_mensagem("Opção inválida.")

    def relatorio_clube(self):
        if not self.__clube_selecionado:
            self.__tela_clube.mostra_mensagem("Nenhum clube selecionado!")
            return
        
        self.__tela_clube.relatorio_clube(
            self.__clube_selecionado,
            self.__clube_selecionado.jogadores,
            self.__clube_selecionado.campeonatos
        )

    def jogador_maior_salario(self):
        if not self.__clube_selecionado.jogadores:
            self.__tela_clube.mostra_mensagem("O clube não possui jogadores!")
            return
        
        maior_salario_jogador = max(self.__clube_selecionado.jogadores, key=lambda c: c.salario)
        self.__tela_clube.relatorio_maior_salario(maior_salario_jogador.jogador)

    def jogador_menor_salario(self):
        if not self.__clube_selecionado.jogadores:
            self.__tela_clube.mostra_mensagem("O clube não possui jogadores!")
            return
        
        menor_salario_jogador = min(self.__clube_selecionado.jogadores, key=lambda c: c.salario)
        self.__tela_clube.relatorio_menor_salario(menor_salario_jogador.jogador)

    def jogador_maior_multa(self):
        if not self.__clube_selecionado.jogadores:
            self.__tela_clube.mostra_mensagem("O clube não possui jogadores!")
            return
        
        maior_multa_jogador = max(self.__clube_selecionado.jogadores, key=lambda c: c.multa_rescisoria)
        self.__tela_clube.relatorio_maior_multa(maior_multa_jogador.jogador)

    def jogador_menor_multa(self):
        if not self.__clube_selecionado.jogadores:
            self.__tela_clube.mostra_mensagem("O clube não possui jogadores!")
            return
        
        menor_multa_jogador = min(self.__clube_selecionado.jogadores, key=lambda c: c.multa_rescisoria)
        self.__tela_clube.relatorio_menor_multa(menor_multa_jogador.jogador)

    def retornar_menu_clube_selecionado(self):
        # Retorna ao menu do clube selecionado
        self.tela_clube_selecionado()

    def retornar_menu_principal(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        opcoes = {
            1: self.selecionar_clube,
            2: self.cadastrar_clube,
            3: self.alterar_clube,
            4: self.listar_clubes,
            5: self.excluir_clube,
            0: self.retornar_menu_principal
        }

        while True:
            opcao = self.__tela_clube.tela_inicial_clube()
            acao = opcoes.get(opcao)
            if acao:
                acao()
            else:
                self.__tela_clube.mostra_mensagem("Opção inválida.")
