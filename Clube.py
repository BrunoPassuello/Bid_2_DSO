from Jogador import Jogador
from Cidade import Cidade
from Tecnico import Tecnico
from Campeonato import Campeonato
class Clube:
    def __init__(self, nome : str, cidade : Cidade):
        self.__nome = nome
        self.__jogadores = []
        self.__cidade = cidade
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
    def cidade(self):
        return self.__cidade
    
    @cidade.setter
    def cidade(self, cidade):
        self.__cidade = cidade
        
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
        from ContratoJogador import ContratoJogador
        contrato = ContratoJogador(self, jogador, salario, multa_rescisoria, contrato_produtividade)
        jogador.contrato = contrato
        self.__jogadores.append(contrato)
        
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
        for contrato in self.__jogadores:
            print(contrato.jogador.nome)
    
    def contratar_tecnico(self, tecnico : Tecnico, salario : float, multa_rescisoria : float):
        from ContratoTecnico import ContratoTecnico
        contrato = ContratoTecnico(self, tecnico, salario, multa_rescisoria)
        tecnico.contrato = contrato
        self.__contrato_tecnico = contrato
    
    def alterar_contrato_tecnico(self, salario : float, multa_rescisoria : float):
        from ContratoTecnico import ContratoTecnico
        contrato = ContratoTecnico(self, self.__contrato_tecnico.tecnico, salario, multa_rescisoria)
        self.__contrato_tecnico = contrato
        
    def demitir_tecnico(self):
        self.__contrato_tecnico.tecnico.contrato = None
        self.__contrato_tecnico = None
        print("Técnico demitido com sucesso!")    
    
    def listar_contrato_tecnico(self):
        if self.__contrato_tecnico == None:
            return print("Clube não possui técnico!")
        print("INFORMAÇÕES PESSOAIS DE TÉCNICO:")
        print("Nome: " + self.__contrato_tecnico.tecnico.nome)
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
        self.__campeonatos.append(campeonato)
        campeonato.clubes.append(self)
    
    def sair_campeonato(self, campeonato : Campeonato):
        self.__campeonatos.remove(campeonato)
        campeonato.clubes.remove(self)
    
    def jogador_maior_salario(self):
        maior_salario = 0
        jogador = None
        for contrato in self.__jogadores:
            if contrato.salario > maior_salario:
                maior_salario = contrato.salario
                jogador = contrato.jogador
        return jogador.nome
    
    def jogador_maior_multa(self):
        maior_multa = 0
        jogador = None
        for contrato in self.__jogadores:
            if contrato.multa_rescisoria > maior_multa:
                maior_multa = contrato.multa_rescisoria
                jogador = contrato.jogador
        return jogador.nome 