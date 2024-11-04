from entidades.contrato_tecnico import ContratoTecnico
from excecoes.cpf_invalido_error import CpfInvalidoError
from excecoes.salario_invalido_error import SalarioInvalidoError
from excecoes.multa_rescisoria_invalida_error import MultaRescisoriaInvalidaError
from telas.tela_contrato_tecnico import TelaContratoTecnico

class ControladorContratoTecnico:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema 
        self.__tela_contrato_tecnico = TelaContratoTecnico()
        self.__contratos = []

    def contratar_tecnico(self):
        try:
            dados_contrato = self.__tela_contrato_tecnico.pega_dados_contrato()
            tecnico = self.__controlador_sistema.controlador_tecnico.pega_tecnico_por_cpf(dados_contrato["cpf"])

            if tecnico is None:
                self.__tela_contrato_tecnico.mostra_mensagem("Técnico não encontrado!")
                return

            contrato = ContratoTecnico(
                clube = self.__controlador_sistema.pega_clube_selecionado,
                tecnico=tecnico,
                salario=dados_contrato["salario"],
                multa_rescisoria=dados_contrato["multa_rescisoria"]
            )
            tecnico.contrato = contrato
            self.__contratos.append(tecnico.contrato)
            self.__tela_contrato_tecnico.mostra_mensagem("Contrato criado com sucesso.")
        except (CpfInvalidoError, SalarioInvalidoError, MultaRescisoriaInvalidaError) as e:
            self.__tela_contrato_tecnico.mostra_mensagem(str(e))

    def alterar_contrato_tecnico(self):
        try:
            dados_contrato = self.__tela_contrato_tecnico.pega_dados_contrato()
            tecnico = self.__controlador_sistema.controlador_tecnico.pega_tecnico_por_cpf(dados_contrato["cpf"])

            if tecnico is None or tecnico.contrato is None:
                self.__tela_contrato_tecnico.mostra_mensagem("Técnico ou contrato não encontrado!")
                return

            tecnico.contrato.salario = dados_contrato["salario"]
            tecnico.contrato.multa_rescisoria = dados_contrato["multa_rescisoria"]
            self.__tela_contrato_tecnico.mostra_mensagem("Contrato alterado com sucesso.")
        except (CpfInvalidoError, SalarioInvalidoError, MultaRescisoriaInvalidaError) as e:
            self.__tela_contrato_tecnico.mostra_mensagem(str(e))

    def demitir_tecnico(self):
        try:
            cpf = (input("CPF do técnico a ser demitido: "))
            if not (len(cpf) == 11):
                raise CpfInvalidoError()
            tecnico = self.__controlador_sistema.controlador_tecnico.pega_tecnico_por_cpf(cpf)

            if tecnico is None or tecnico.contrato is None:
                self.__tela_contrato_tecnico.mostra_mensagem("Técnico ou contrato não encontrado!")
                return

            self.__contratos.remove(tecnico.contrato)
            tecnico.contrato = None
            self.__tela_contrato_tecnico.mostra_mensagem("Contrato encerrado e técnico demitido.")
        except CpfInvalidoError as e:
            self.__tela_contrato_tecnico.mostra_mensagem(str(e))
        except ValueError:
            self.__tela_contrato_tecnico.mostra_mensagem("Erro: CPF inválido.")

    def abre_tela(self):
        lista_opcoes = {
            1: self.contratar_tecnico,
            2: self.alterar_contrato_tecnico,
            3: self.demitir_tecnico,
            4: self.listar_contratos,
            0: self.__controlador_sistema.abre_tela  # Opção para retornar ao controlador do sistema
        }

        while True:
            opcao = self.__tela_contrato_tecnico.tela_opcoes()
            funcao_escolhida = lista_opcoes.get(opcao)
            if funcao_escolhida:
                funcao_escolhida()
            else:
                self.__tela_contrato_tecnico.mostra_mensagem("Opção inválida.")
    def listar_contratos(self):
        if len(self.__contratos) == 0:
            self.__tela_contrato_tecnico.mostra_mensagem("Nenhum contrato de técnico registrado.")
            return

        for contrato in self.__contratos:
            self.__tela_contrato_tecnico.mostra_contrato(contrato)