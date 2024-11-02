from entidades.contrato_jogador import ContratoJogador

class ControladorContratoJogador:
    def __init__(self):
        self.contratos = []

    def adicionar_contrato(self, contrato: ContratoJogador):
        self.contratos.append(contrato)

    def remover_contrato(self, contrato: ContratoJogador):
        if contrato in self.contratos:
            self.contratos.remove(contrato)

    def buscar_contrato_por_jogador(self, jogador_id: int):
        for contrato in self.contratos:
            if contrato.jogador_id == jogador_id:
                return contrato
        return None

    def listar_contratos(self):
        return self.contratos

    def atualizar_contrato(self, contrato_atualizado: ContratoJogador):
        for idx, contrato in enumerate(self.contratos):
            if contrato.id == contrato_atualizado.id:
                self.contratos[idx] = contrato_atualizado
                return True
        return False