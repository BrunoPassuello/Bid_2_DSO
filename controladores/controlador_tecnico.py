from telas.tela_tecnico import TelaTecnico
from entidades.Tecnico import Tecnico

class ControladorTecnico:
    def __init__(self, controlador_sistema):
        self.__tecnicos = []
        self.__tela_tecnico = TelaTecnico()
        self.__controlador_sistema = controlador_sistema
    
    def pega_tecnico_por_cpf(self, cpf):
        for tecnico in self.__tecnicos:
            if tecnico.cpf == cpf:
                return tecnico
        return None

    def incluir_tecnico(self): #VERIFICAÇÕES!!!!
        dados_tecnico = self.__tela_tecnico.tela_cadastro_tecnico()
        tecnico = Tecnico(
        dados_tecnico["nome"], 
        dados_tecnico["cpf"],
        dados_tecnico["idade"],
        dados_tecnico["cidade"],
        dados_tecnico["licenca"])
        self.__tecnicos.append(tecnico)

    def alterar_tecnico(self):
        self.listar_tecnico()
        cpf = self.__tela_tecnico.seleciona_tecnico()
        tecnico = self.pega_tecnico_por_cpf(cpf)
        if tecnico is not None:
            dados_tecnico = self.__tela_tecnico.tela_cadastro_tecnico()
            tecnico.nome = dados_tecnico["nome"]
            tecnico.idade = dados_tecnico["idade"]
            tecnico.cidade = dados_tecnico["cidade"]
            tecnico.licenca = dados_tecnico["licenca"]
        else:
            print("ATENÇÃO: Técnico não encontrado!")

    def excluir_tecnico(self):
        self.listar_tecnico()
        cpf = self.__tela_tecnico.seleciona_tecnico()
        tecnico = self.pega_tecnico_por_cpf(cpf)
        if tecnico is not None:
            self.__tecnicos.remove(tecnico)
        else:
            print("ATENÇÃO: Técnico não encontrado!")
    
    def listar_tecnico(self):
        self.__tela_tecnico.mostra_tecnico(self.__tecnicos)
    
    def retornar(self):
        self.__controlador_sistema.abre_tela()
    
    def abre_tela(self):
        lista_opcoes = {
            1: self.incluir_tecnico,
            2: self.alterar_tecnico,
            3: self.listar_tecnico,
            4: self.excluir_tecnico,
            0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_tecnico.tela_inicial_tecnico()]()

