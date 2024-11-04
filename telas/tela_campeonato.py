
class TelaCampeonato():
    def tela_inicial_campeonato(self):
        mensagem = '''
        ----------CAMPEONATO---------

        Escolha uma Opção:

        * Cadastrar Campeonato - 1
        * Alterar Campeonato - 2
        * Listar Campeonatos - 3
        * Excluir Campeonato - 4
        * Retornar - 0
        '''
        print(mensagem)
        try:
            comando = int(input("Escolha sua opção: "))
            if comando in range(5):
                return comando
            else:
                self.mostra_mensagem("Opção inválida! Por favor, escolha um número entre 0 e 4.")
                return self.tela_inicial_campeonato()
        except ValueError:
            self.mostra_mensagem("Entrada inválida! Por favor, insira um número.")
            return self.tela_inicial_campeonato()
        
    
    def tela_cadastro_campeonato(self):
        mensagem = '''
        ----------CADASTRO CAMPEONATO---------

        Digite as informações do campeonato:

        '''
        print(mensagem)
        nome = input("Nome: ")
        try:
            premiacao = int(input("Premiação: "))
            numero_times = int(input("Número de times: "))
            numero_estrangeiros = int(input("Número de estrangeiros por time: "))
            numero_jogadores = int(input("Número de jogadores por time: "))
        except ValueError:
            print("Entrada inválida! Insira um número.")
            self.tela_cadastro_campeonato()

        #VERIFICAÇÕES

        return {
            "nome": nome,
            "premiacao": premiacao,
            "numero_times": numero_times,
            "numero_estrangeiros": numero_estrangeiros,
            "numero_jogadores": numero_jogadores
        }
    
    def seleciona_campeonato(self):
        mensagem = '''
        ----------SELECIONAR CAMPEONATO---------

        Digite o nome do campeoanto:
        '''
        print(mensagem)
        nome = input("Nome: ")
        return nome
    
    def mostra_campeonato(self, lista_campeonatos):
        mensagem = '''
        ----------CAMPEONATOS CADASTRADOS---------
        '''
        print(mensagem)
        for campeonato in lista_campeonatos:
            print("")
            print("Nome: ", campeonato.nome)
            print("Premiação: ", campeonato.premiacao)
            print("Número de times: ", campeonato.regra.numero_times)
            print("Número de estrangeiros por time: ", campeonato.regra.numero_estrangeiros)
            print("Número de jogadores por time: ", campeonato.regra.numero_jogadores)
    
    def mostra_mensagem(self, mensagem):
        print(mensagem)