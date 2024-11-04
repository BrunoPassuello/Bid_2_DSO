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
        try:
            comando = int(input("Escolha sua opção: "))
            if comando in range(5):
                return comando
            else:
                self.mostra_mensagem("Opção inválida! Por favor, escolha um número entre 0 e 4.")
                return self.tela_inicial_tecnico()
        except ValueError:
            self.mostra_mensagem("Entrada inválida! Por favor, insira um número.")
            return self.tela_inicial_tecnico()

    def tela_cadastro_tecnico(self):
        mensagem = '''
        ----------CADASTRO TÉCNICO---------

        Digite as informações do técnico:

        '''
        print(mensagem)
        nome = input("Nome: ")
        cpf = input("CPF: ")
        idade = input("Idade: ")
        pais = input("País: ")
        licenca = input("Licença: ") 
        #VERIFICAR LICENCA E STR, INT.
        return {"nome": nome,
                "cpf": cpf,
                "idade": idade,
                "pais": pais,
                "licenca": licenca}
    
    def seleciona_tecnico(self):
        mensagem = '''
        ----------SELECIONAR TÉCNICO---------

        Digite o CPF do técnico:
        '''
        print(mensagem)
        cpf = input("CPF: ")
        return cpf
    
    def mostra_tecnico(self, lista_tecnicos):
        mensagem = '''
        ----------TÉCNICOS CADASTRADOS---------
        '''
        print(mensagem)
        for tecnico in lista_tecnicos:
            print("")
            print("Nome: ", tecnico.nome)
            print("CPF: ", tecnico.cpf)
            print("Idade: ", tecnico.idade)
            print("País: ", tecnico.pais)
            print("Licença: ", tecnico.licenca.tipo)

    def mostra_mensagem(self, mensagem):
        print(mensagem)