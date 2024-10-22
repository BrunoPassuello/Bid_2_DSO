from telas.tela_tecnico import TelaTecnico
from entidades.Tecnico import Tecnico

class ControladorTecnico:
    def __init__(self, controlador_sistema):
        self.__tecnicos = []
        self.__tela_tecnico = TelaTecnico()
        self.__controlador_sistema = controlador_sistema
    
    def incluir_tecnico(self, dados_tecnico):
        dados_tecnico = self.__tela_tecnico.tela_cadastro_tecnico()
        tecnico = Tecnico(
        dados_tecnico["nome"], 
        dados_tecnico["cpf"],
        dados_tecnico["idade"],
        dados_tecnico["cidade"],
        dados_tecnico["licenca"])
        self.__tecnicos.append(tecnico)



    def retornar(self):
        self.__controlador_sistema.abre_tela()
    
    def abre_tela(self):
        lista_opcoes = {1: self.incluir_amigo, 2: self.alterar_amigo, 3: self.lista_amigos, 4: self.excluir_amigo, 0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_amigo.tela_opcoes()]()

