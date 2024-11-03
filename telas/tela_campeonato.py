
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
        comando = int(input("Escolha sua opção: "))
        return comando
    
    def tela_cadastro_campeonato(self):
        mensagem = '''
        ----------CADASTRO CAMPEONATO---------

        Digite as informações do campeonato:

        '''
        print(mensagem)
        nome = input("Nome: ")
        premiacao = input("Premiação: ")
        numero_times = input("Número de times: ")
        numero_estrangeiros = input("Número de estrangeiros por time: ")
        numero_jogadores = input("Número de jogadores por time: ")

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
            print("Número de times: ", campeonato.numeros_times)
            print("Número de estrangeiros por time: ", campeonato.numeros_estrangeiros)
            print("Número de jogadores por time: ", campeonato.numero_jogadores)
    
    def mostra_mensagem(self, mensagem):
        print(mensagem)