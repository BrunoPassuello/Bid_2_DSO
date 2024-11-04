class TelaJogador():
    def tela_inicial_jogador(self):
        mensagem = '''
        ----------JOGADOR---------

        Escolha uma Opção:

        * Cadastrar Jogador - 1
        * Alterar Jogador - 2
        * Listar Jogadores - 3
        * Excluir Jogadores - 4
        * Retornar - 0
        '''
        print(mensagem)
        try:
            comando = int(input("Escolha sua opção: "))
            if comando in range(5):
                return comando
            else:
                self.mostra_mensagem("Opção inválida! Por favor, escolha um número entre 0 e 4.")
                return self.tela_inicial_jogador()
        except ValueError:
            self.mostra_mensagem("Entrada inválida! Por favor, insira um número.")
            return self.tela_inicial_jogador()
    
    def tela_cadastro_jogador(self):
        mensagem = '''
        ----------CADASTRO JOGADOR---------

        Digite as informações do jogador:

        '''
        print(mensagem)
        nome = input("Nome: ")
        cpf = input("CPF: ")
        idade = input("Idade: ")
        pais = input("País: ")
        posicao = input("Posição: ")
        peso = input("Peso: ")
        altura = input("Altura: ")
        estrangeiro = input("Estrangeiro (S/N): ")
        return {"nome": nome,
                "cpf": cpf,
                "idade": idade,
                "pais": pais,
                "posicao": posicao,
                "peso": peso,
                "altura": altura,
                "estrangeiro": estrangeiro}
    def seleciona_jogador(self):
        mensagem = '''
        ----------SELECIONAR JOGADOR---------

        Digite o CPF do jogador:
        '''
        print(mensagem)
        cpf = input("CPF: ")
        return cpf
    def mostra_jogador(self, lista_jogadores):
        mensagem = '''
        ----------JOGADORES CADASTRADOS---------
        '''
        print(mensagem)
        for jogador in lista_jogadores:
            print("")
            print("Nome: ", jogador.nome)
            print("CPF: ", jogador.cpf)
            print("Idade: ", jogador.idade)
            print("País: ", jogador.pais)
            print("Posição: ", jogador.posicao.nome)
            print("Peso: ", jogador.peso)
            print("Altura: ", jogador.altura)
            print("Estrangeiro: ", jogador.estrangeiro)
    def mostra_mensagem(self, mensagem):
        print(mensagem)