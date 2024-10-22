class TelaSistema:
    def tela_opcoes(self):
        mensagem = '''
        ----------BID_2----------

        Escolha uma Opção:

        * Clube - 1
        * Jogador - 2
        * Técnico - 3
        * Campeonato - 4
        * Finalizar Programa - 0
        '''
        print(mensagem)
        comando = int(input("Escolha sua opção: "))
        return comando