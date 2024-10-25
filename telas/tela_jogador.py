class TelaJogador():
    def tela_inicial_tecnico(self):
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
        comando = int(input("Escolha sua opção: "))
        return comando
    def tela_cadastro_jogador(self):
        mensagem = '''
        ----------CADASTRO JOGADOR---------

        Digite as informações do jogador:

        '''
        print(mensagem)
        nome = input("Nome: ")
        cpf = input("CPF: ")
        idade = input("Idade: ")
        cidade = input("Cidade Natal: ")
        posicao = input("Posição: ")
        peso = input("Peso: ")
        altura = input("Altura: ")
        estrangeiro = input("Estrangeiro (S/N): ")
        return {"nome": nome,
                "cpf": cpf,
                "idade": idade,
                "cidade":cidade,
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
            print("Nome: ", jogador.nome)
            print("CPF: ", jogador.cpf)
            print("Idade: ", jogador.idade)
            print("Cidade: ", jogador.cidade)
            print("Posição: ", jogador.posicao)
            print("Peso: ", jogador.peso)
            print("Altura: ", jogador.altura)
            print("Estrangeiro: ", jogador.estrangeiro)