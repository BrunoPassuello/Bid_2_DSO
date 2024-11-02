class MultaRescisoriaInvalidaError(Exception):
    def __init__(self, mensagem="Multa rescisória inválida. Deve ser um número positivo."):
        super().__init__(mensagem)  # Passa a mensagem para a classe base Exception
