from excecoes.cpf_invalido_error import CpfInvalidoError
from excecoes.salario_invalido_error import SalarioInvalidoError
from excecoes.multa_rescisoria_invalida_error import MultaRescisoriaInvalidaError
from entidades.contrato_jogador import ContratoJogador
from telas.tela_contrato_jogador import TelaContratoJogador

class ControladorContratoJogador:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_contrato_jogador = TelaContratoJogador()

    def abre_tela(self):
        lista_opcoes = {
            1: self.contratar_jogador,
            2: self.alterar_contrato_jogador,
            3: self.demitir_jogador,
            0: self.retornar
        }

        continua = True
        while continua:
            try:
                opcao = self.__tela_contrato_jogador.tela_opcoes()
                if opcao in lista_opcoes:
                    lista_opcoes[opcao]()  # Chama a função correspondente
                else:
                    self.__tela_contrato_jogador.mostra_mensagem("Opção inválida! Tente novamente.")
            except Exception as e:
                self.__tela_contrato_jogador.mostra_mensagem(f"Ocorreu um erro: {str(e)}")

    def retornar(self):
        # Lógica para retornar ao menu anterior
        self.__controlador_sistema.abre_tela()
        print("Retornando ao menu anterior.")

    def contratar_jogador(self):
        try:
            dados_contrato = self.__tela_contrato_jogador.pega_dados_contrato()
            jogador = self.__controlador_sistema.controlador_jogador.pega_jogador_por_cpf(dados_contrato["cpf"])

            if jogador is None:
                self.__tela_contrato_jogador.mostra_mensagem("Erro: Jogador não encontrado para o CPF informado!")
                return

            contrato = ContratoJogador(
                clube=self.__controlador_sistema.clube,
                jogador=jogador,
                salario=dados_contrato["salario"],
                multa_rescisoria=dados_contrato["multa_rescisoria"],
                contrato_produtividade=dados_contrato["contrato_produtividade"]
            )
            jogador.contrato = contrato
            self.__tela_contrato_jogador.mostra_mensagem("Contrato criado com sucesso.")
        except (CpfInvalidoError, SalarioInvalidoError, MultaRescisoriaInvalidaError) as e:
            self.__tela_contrato_jogador.mostra_mensagem(str(e))

    def alterar_contrato_jogador(self):
        try:
            dados_contrato = self.__tela_contrato_jogador.pega_dados_contrato()
            jogador = self.__controlador_sistema.controlador_jogador.pega_jogador_por_cpf(dados_contrato["cpf"])

            if jogador is None or jogador.contrato is None:
                self.__tela_contrato_jogador.mostra_mensagem("Jogador ou contrato não encontrado!")
                return

            jogador.contrato.salario = dados_contrato["salario"]
            jogador.contrato.multa_rescisoria = dados_contrato["multa_rescisoria"]
            jogador.contrato.contrato_produtividade = dados_contrato["contrato_produtividade"]
            self.__tela_contrato_jogador.mostra_mensagem("Contrato alterado com sucesso.")
        except (CpfInvalidoError, SalarioInvalidoError, MultaRescisoriaInvalidaError) as e:
            self.__tela_contrato_jogador.mostra_mensagem(str(e))

    def demitir_jogador(self):
        try:
            cpf = int(input("CPF do jogador a ser demitido: "))
            if not (isinstance(cpf, int) and len(str(cpf)) == 11):
                raise CpfInvalidoError()
            jogador = self.__controlador_sistema.controlador_jogador.pega_jogador_por_cpf(cpf)

            if jogador is None or jogador.contrato is None:
                self.__tela_contrato_jogador.mostra_mensagem("Jogador ou contrato não encontrado!")
                return

            jogador.contrato = None
            self.__tela_contrato_jogador.mostra_mensagem("Contrato encerrado e jogador demitido.")
        except CpfInvalidoError as e:
            self.__tela_contrato_jogador.mostra_mensagem(str(e))
        except ValueError:
            self.__tela_contrato_jogador.mostra_mensagem("Erro: CPF inválido.")
