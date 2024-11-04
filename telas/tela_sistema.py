class TelaSistema:
    def tela_opcoes(self):
        while True:
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
            try:
                comando = int(input("Escolha sua opção: "))
                if comando in range(6):  # 0 a 5
                    return comando
                else:
                    print("Opção inválida! Por favor, escolha um número entre 0 e 5.")
            except ValueError:
                print("Entrada inválida! Por favor, digite um número.")
