class ChaveInvalidaError(Exception):
    def __init__(self, mensagem="Chave inválida. Coloque uma chave existente."):
        super().__init__(mensagem)
