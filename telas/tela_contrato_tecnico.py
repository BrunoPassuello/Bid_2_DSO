from excecoes.cpf_invalido_error import CpfInvalidoError
from excecoes.salario_invalido_error import SalarioInvalidoError
from excecoes.multa_rescisoria_invalida_error import MultaRescisoriaInvalidaError

class TelaContratoTecnico:
    def tela_opcoes(self):
        print("------ Menu Contrato do Técnico ------")
        print("1: Contratar Técnico")
        print("2: Alterar Contrato do Técnico")
        print("3: Demitir Técnico")
        print("0: Retornar")
        try:
            opcao = int(input("Escolha a opção: "))
            return opcao
        except ValueError:
            print("Opção inválida! Digite um número.")
            return self.tela_opcoes()

    def pega_dados_contrato(self):
        print("---- Dados do Contrato do Técnico ----")
        cpf = input("CPF do técnico (somente números): ")
        if not cpf.isdigit() or len(cpf) != 11:
            raise CpfInvalidoError()
        
        try:
            salario = float(input("Salário do técnico: "))
            if salario <= 0:
                raise SalarioInvalidoError()
        except ValueError:
            raise SalarioInvalidoError("Salário inválido. Insira um número positivo.")

        try:
            multa_rescisoria = float(input("Multa rescisória: "))
            if multa_rescisoria < 0:
                raise MultaRescisoriaInvalidaError()
        except ValueError:
            raise MultaRescisoriaInvalidaError("Multa rescisória inválida. Insira um número.")

        return {
            "cpf": cpf,
            "salario": salario,
            "multa_rescisoria": multa_rescisoria
        }

    def mostra_mensagem(self, mensagem):
        print(mensagem)
