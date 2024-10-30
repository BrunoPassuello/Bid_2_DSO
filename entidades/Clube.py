from entidades.Jogador import Jogador
from entidades.Pais import Pais
from entidades.Tecnico import Tecnico
from entidades.Campeonato import Campeonato
class Clube:
    def __init__(self, nome : str, pais : Pais):
        self.__nome = nome
        self.__jogadores = []
        self.__pais = pais
        self.__contrato_tecnico = None
        self.__campeonatos = []
    
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
        
    @property
    def jogadores(self):
        return self.__jogadores
    
    @property
    def pais(self):
        return self.__pais
    
    @pais.setter
    def pais(self, pais):
        self.__pais = pais
        
    @property
    def contrato_tecnico(self):
        return self.__contrato_tecnico
    
    @contrato_tecnico.setter
    def contrato_tecnico(self, tecnico):
        self.__contrato_tecnico = tecnico
        
    @property
    def campeonatos(self):
        return self.__campeonatos
    
        
    def contratar_jogador(self, jogador : Jogador, salario : float, multa_rescisoria : float, contrato_produtividade : bool):
        from entidades.ContratoJogador import ContratoJogador
        if jogador.contrato != None:
            print("Jogador já possui contrato!")
        else:
            contrato = ContratoJogador(self, jogador, salario, multa_rescisoria, contrato_produtividade)
            jogador.contrato = contrato
            self.__jogadores.append(contrato)
            print("Jogador contratado com sucesso!")
        
    def alterar_contrato_jgoador(self, jogador : Jogador, salario : float, multa_rescisoria : float, contrato_produtividade : bool):
        for contrato in self.__jogadores:
            if contrato.jogador == jogador:
                contrato.salario = salario
                contrato.multa_rescisoria = multa_rescisoria
                contrato.contrato_produtividade = contrato_produtividade
                
    def informacoes_jogador(self, jogador : Jogador):
        for contrato in self.__jogadores:
            if contrato.jogador == jogador:
                print("INFORMAÇÕES PESSOAIS DE JOGADOR:")
                print("Nome: " + contrato.jogador.nome)
                print("CPF: " + str(contrato.jogador.cpf))
                print("Idade: " + str(contrato.jogador.idade))
                print("Cidade de nascimento: " + contrato.jogador.cidade.nome)
                print("Altura (M): " + str(contrato.jogador.altura))
                print("Peso (KG): " + str(contrato.jogador.peso))
                print("INFORMAÇÕES DO CONTRATO:")
                print("Clube: " + contrato.clube.nome)
                print("Salário: " + str(contrato.salario))
                print("Multa rescisória: " + str(contrato.multa_rescisoria))
                print("Contrato de produtividade: " + str(contrato.contrato_produtividade))
                break
        
    def demitir_jogador(self, jogador : Jogador):
        for contrato in self.__jogadores:
            if contrato.jogador == jogador:
                self.__jogadores.remove(contrato)
                jogador.contrato = None
                print("Jogador demitido com sucesso!")
                break
    
    def listar_jogadores(self):
        jogadores_ordenados = sorted(self.__jogadores, key = lambda x: x.jogador.nome)
        for contrato in jogadores_ordenados:
            print(contrato.jogador.nome)
    
    def contratar_tecnico(self, tecnico : Tecnico, salario : float, multa_rescisoria : float):
        if tecnico.contrato != None:
            return print("Técnico já possui contrato!")
        else:
            from entidades.ContratoTecnico import ContratoTecnico
            contrato = ContratoTecnico(self, tecnico, salario, multa_rescisoria)
            tecnico.contrato = contrato
            self.__contrato_tecnico = contrato
            return print("Técnico contratado com sucesso!")
    
    def alterar_contrato_tecnico(self, salario : float, multa_rescisoria : float):
        from entidades.ContratoTecnico import ContratoTecnico
        contrato = ContratoTecnico(self, self.__contrato_tecnico.tecnico, salario, multa_rescisoria)
        self.__contrato_tecnico = contrato
        return print("Contrato de técnico alterado com sucesso!")
        
    def demitir_tecnico(self):
        self.__contrato_tecnico.tecnico.contrato = None
        self.__contrato_tecnico = None
        return print("Técnico demitido com sucesso!")    
    
    def listar_contrato_tecnico(self):
        if self.__contrato_tecnico == None:
            return print("Clube não possui técnico!")
        print("INFORMAÇÕES PESSOAIS DE TÉCNICO:")
        print("Nome: " + self.__contrato_tecnico.tecnico.nome)
        print("CPF: " + str(self.__contrato_tecnico.tecnico.cpf))
        print("Idade: " + str(self.__contrato_tecnico.tecnico.idade))
        print("Cidade de nascimento: " + self.__contrato_tecnico.tecnico.cidade.nome)
        print("Licença: " + self.__contrato_tecnico.tecnico.licenca.tipo)
        print("INFORMAÇÕES CONTRATUAIS:")
        print("Clube: " + self.__contrato_tecnico.clube.nome)
        print("Salário: " + str(self.__contrato_tecnico.salario))
        print("Multa rescisória: " + str(self.__contrato_tecnico.multa_rescisoria))
    
    def tecnico(self):
            if self.__contrato_tecnico == None:
                return print("Clube não possui técnico!")
            return self.__contrato_tecnico.tecnico.nome
        
    def entrar_campeonato(self, campeonato : Campeonato):
        estrangeiros = 0
        for jogador in self.__jogadores:
            if jogador.jogador.estrangeiro:
                estrangeiros += 1
        if campeonato.regra.numero_estrangeiros < estrangeiros:
            return print("Clube não pode entrar no campeonato, número de estrangeiros excedido!")
        else:
            self.__campeonatos.append(campeonato)
            campeonato.clubes.append(self)
            return print("Clube entrou no campeonato com sucesso!")
    
    def sair_campeonato(self, campeonato : Campeonato):
        self.__campeonatos.remove(campeonato)
        campeonato.clubes.remove(self)
        return print("Clube saiu do campeonato com sucesso!")
    
    def jogador_maior_salario(self):
        if len(self.__jogadores) > 0:
            maior_salario = 0
            jogador = None
            for contrato in self.__jogadores:
                if contrato.salario > maior_salario:
                    maior_salario = contrato.salario
                    jogador = contrato.jogador
            return jogador.nome
        else:
            return print("Clube não possui jogadores!")
    
    def jogador_menor_salario(self):
        if len(self.__jogadores) > 0:
            menor_salario = 99999999999999999999999999999999
            jogador = None
            for contrato in self.__jogadores:
                if contrato.salario < menor_salario:
                    menor_salario = contrato.salario
                    jogador = contrato.jogador
            return jogador.nome
        else:
            return print("Clube não possui jogadores!")
    
    def jogador_maior_multa(self):
        if len(self.__jogadores) > 0:
            maior_multa = 0
            jogador = None
            for contrato in self.__jogadores:
                if contrato.multa_rescisoria > maior_multa:
                    maior_multa = contrato.multa_rescisoria
                    jogador = contrato.jogador
            return jogador.nome 
        else:
            return print("Clube não possui jogadores!")
        
    def jogador_menor_multa(self):
        if len(self.__jogadores) > 0:
            menor_multa = 99999999999999999999999999999999
            jogador = None
            for contrato in self.__jogadores:
                if contrato.multa_rescisoria < menor_multa:
                    menor_multa = contrato.multa_rescisoria
                    jogador = contrato.jogador
            return jogador.nome
        else:
            return print("Clube não possui jogadores!")
    
    def relatorio(self):
        nome = self.__nome.upper()
        print("RELATÓRIO DO CLUBE " + nome + ":")
        print("Cidade: " + self.__cidade.nome)
        print("Estado: " + self.__cidade.estado.nome)
        print("País: " + self.__cidade.estado.pais.nome)
        if len(self.__jogadores) > 0:
            print("JOGADORES:")
            self.listar_jogadores()
        if self.__contrato_tecnico != None:
            print("TÉCNICO: " + self.__contrato_tecnico.tecnico.nome)
        if len(self.__campeonatos) > 0:
            print("CAMPEONATOS:")
            for campeonato in self.__campeonatos:
                print(campeonato.nome)
        print("MAIOR SALÁRIO: " + self.jogador_maior_salario())
        print("MENOR SALÁRIO: " + self.jogador_menor_salario())
        print("MAIOR MULTA: " + self.jogador_maior_multa())
        print("MENOR MULTA: " + self.jogador_menor_multa())
        
    def listar_cameponatos(self):
        if len(self.__campeonatos) > 0:
            print("CAMPEONATOS:")
            self.__campeonatos.sort(key = lambda x: x.nome)
            for campeonato in self.__campeonatos:
                print(campeonato.nome)
        else:
            print("Clube não está em nenhum campeonato!")