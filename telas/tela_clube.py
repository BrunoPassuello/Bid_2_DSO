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

    def relatorio_clube(self, clube):
        mensagem = '''
        ----------RELATÓRIO DO CLUBE ''' + clube.nome + '''---------
        Nome: 
        '''
    #TERMINAR RELATÓRIO DO CLUBE E O RESTO DOS MÉTODOS DE INFORMAÇÕES
