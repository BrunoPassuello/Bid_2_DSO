from excecoes.cpf_invalido_error import CpfInvalidoError
from excecoes.salario_invalido_error import SalarioInvalidoError
from excecoes.multa_rescisoria_invalida_error import MultaRescisoriaInvalidaError

class TelaContratoJogador:
    def tela_opcoes(self):
        print("------ Menu Contrato do Jogador ------")
        print("1: Contratar Jogador")
        print("2: Alterar Contrato de Jogador")
        print("3: Demitir Jogador")
        print("4: Listar Contratos de Jogador")
        print("0: Retornar")
        try:
            opcao = int(input("Escolha a opção: "))
            return opcao
        except ValueError:
            print("Opção inválida! Digite um número.")
            return self.tela_opcoes()

    def pega_dados_contrato(self):
        print("---- Dados do Contrato ----")
        
#como o sistema é hipotético vou fazer uma validação simples de cpf, pensei em usar aquela lib mas não sei se pode
        cpf = input("CPF do jogador (somente números): ")
        if not cpf.isdigit() or len(cpf) != 11:
            raise CpfInvalidoError()
        
# validando o salário
        try:
            salario = float(input("Salário do jogador: "))
            if salario <= 0:
                raise SalarioInvalidoError()
        except ValueError:
            raise SalarioInvalidoError("Salário inválido. Insira um número.")
# Aqui to só fazendo a verificação da multa rescisória, mas o contrato de produtividade não precisa de verificação
        try:
            multa_rescisoria = float(input("Multa rescisória: "))
            if multa_rescisoria < 0:
                raise MultaRescisoriaInvalidaError()
        except ValueError:
            raise MultaRescisoriaInvalidaError("Multa rescisória inválida. Insira um número.")

        contrato_produtividade = input("Contrato de produtividade (S/N): ").upper() == "S"
        
        return {
            "cpf": cpf,
            "salario": salario,
            "multa_rescisoria": multa_rescisoria,
            "contrato_produtividade": contrato_produtividade
        }

    def mostra_mensagem(self, mensagem):
        print(mensagem)
    def mostra_contrato(self, contrato):
        print(
            "Nome: ", contrato.jogador.nome,
            "CPF: ", contrato.jogador.cpf,
            "Salário: ", contrato.salario,
            "Multa Rescisória: ", contrato.multa_rescisoria,
            "Contrato de Produtividade: ", contrato.contrato_produtividade
        )