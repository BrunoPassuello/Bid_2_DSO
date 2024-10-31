class TelaClube():
    def tela_inicial_clube(self):
        mensagem = '''
        ----------CLUBE---------

        Escolha uma Opção:

        * Selecionar Clube - 1
        * Cadastrar Clube - 2
        * Alterar Clube - 3
        * Listar Clubes - 4
        * Excluir Clube - 5
        * Retornar - 0
        '''
        print(mensagem)
        comando = int(input("Escolha sua opção: "))
        return comando
    
    def tela_clube_selecionado(self): #Verificar se isso ta saindo certo
        mensagem = '''
        ----------CLUBE---------

        Escolha uma Área para Operar:

        * Jogador - 1
        * Técnico - 2
        * Campeonato - 3
        * Informações do Clube - 4
        * Retornar - 0
        '''

        print(mensagem)
        comando = int(input("Escolha sua opção: "))
        return comando

    def tela_clube_informacoes(self):
        mensagem = '''
        ----------CLUBE SELECIONADO---------

        * INFORMAÇÕES DO CLUBE *

        Escolha uma Opção:

        * Relatório do clube - 1
        * Jogador com maior Salário - 2
        * Jogador com menor Salário - 3
        * Jogador com maior Multa - 4
        * Jogador com menor Multa - 5
        * Retornar - 0
        '''
        print(mensagem)
        comando = int(input("Escolha sua opção: "))
        return comando

    def tela_clube_campeonato(self):
        mensagem = '''
        ----------CLUBE SELECIONADO---------

        * OPERAÇÃO DE CAMPEONATOS *

        Escolha uma Opção:

        * Participar de Campeonato - 1
        * Sair de Campeonato - 2
        * Listar Campeonatos - 3
        * Campeonato com maior premiação - 4
        * Retornar - 0
        '''
        print(mensagem)
        comando = int(input("Escolha sua opção: "))
        return comando

    def tela_clube_tecnico(self):
        mensagem = '''
        ----------CLUBE SELECIONADO---------

        * OPERAÇÃO DE TÉCNICOS *

        Escolha uma Opção:

        * Contratar Técnico - 1
        * Alterar Contrato de Técnico - 2
        * Relatório do Técnico - 3
        * Demitir Técnico - 4
        * Retornar - 0
        '''
        print(mensagem)
        comando = int(input("Escolha sua opção: "))
        return comando
    
    def tela_clube_jogador(self):
        mensagem = '''
        ----------CLUBE SELECIONADO---------

        * OPERAÇÃO DE JOGADORES *

        Escolha uma Opção:

        * Contratar Jogador - 1
        * Alterar Contrato de Jogador - 2
        * Listar Jogadores - 3
        * Demitir Jogador - 4
        * Retornar - 0
        '''
        print(mensagem)
        comando = int(input("Escolha sua opção: "))
        return comando

    def tela_cadastra_clube(self):
        mensagem = '''
        ----------CADASTRO CLUBE---------

        Digite as informações do clube:

        '''
        print(mensagem)
        nome = input("Nome: ")
        pais = input("País")
        return {
            "nome": nome,
            "pais": pais
        }

    def seleciona_clube(self):
        mensagem = '''
        ----------SELECIONAR CLUBE---------

        Digite o Nome do clube:
        '''
        print(mensagem)
        nome = input("Nome: ")
        return nome
    
    def mostra_clube(self, lista_clubes):
        mensagem = '''
        ----------CLUBES CADASTRADOS---------
        '''
        print(mensagem)
        for clube in lista_clubes:
            print("")
            print("Nome: ", clube.nome)
            print("País: ", clube.pais)

    #CPA DA PRA FAZER DIFERENTE ISSO AQ
    def relatorio_clube(self, clube, lista_contrato_jogadores, lista_campeonatos):
        mensagem = '''
        ----------RELATÓRIO DO CLUBE ''' + clube.nome + '''---------'''
        
        print(mensagem)
        print("Nome: " + clube.nome)
        print("Páis: " + clube.pais)
        if clube.contrato_tecnico is not None:
            print("Técnico: " + clube.contrato_tecnico.tecnico.nome)
        else:
            print("O clube não possui técnico!")
        if len(lista_contrato_jogadores) >= 1:
            print("------JOGADORES------")
            for contrato_jogador in lista_contrato_jogadores:
                print("")
                print("Nome: " + contrato_jogador.jogador.nome)
                print("Salário: " + contrato_jogador.salario)
                print("Multa Rescisória: " + contrato_jogador.multa_rescisoria)
        else:
            print("O clube não possui jogadores!")
        if len(lista_campeonatos) >= 1:
            print("------CAMPEONATOS------")
            for campeonato in lista_campeonatos:
                print("")
                print("Nome: " + campeonato.nome)
                print("Premiação: " + campeonato.premiacao)
        else:
            print("O Clube não está participando de nenhum campeonato!")
    
    def relatorio_maior_salario(self, jogador):
        #metodo no controlador procura o maior salario, e manda o jogador pra esse metodo
        print("Jogador com maior salário: " + jogador.nome)
    
    def relatorio_menor_salario(self, jogador):
        print("Jogador com menor salário: " + jogador.nome)

    def relatorio_maior_multa(self, jogador):
        print("Jogador com maior multa: " + jogador.nome)

    def relatorio_menor_multa(self, jogador):
        print("Jogador com menor multa: " + jogador.nome)
    
