class TelaTecnico():
    def tela_inicial_tecnico(self):
        mensagem = '''
        ----------TÉCNICO---------

        Escolha uma Opção:

            * Cadastrar Técnico - 1
            * Alterar Técnico - 2
            * Listar Técnicos - 3
            * Excluir Técnicos - 4
            * Retornar - 0
        '''
        print(mensagem)
        comando = input("Escolha sua opção: ")
        return comando

    def tela_cadastro_tecnico(self):
        mensagem = '''
        ----------CADASTRO TÉCNICO---------

        Digite as informações do técnico:

        '''
        print(mensagem)
        nome = input("Nome: ")
        cpf = input("CPF: ")
        idade = input("Idade: ")
        cidade = input("Cidade Natal: ")
        licenca = input("Licença: ") 
        #VERIFICAR LICENCA E STR, INT.
        return {"nome": nome,
                "cpf": cpf,
                "idade": idade,
                "cidade":cidade,
                "licenca": licenca}