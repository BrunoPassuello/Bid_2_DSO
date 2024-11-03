class CpfInvalidoError(Exception):
    def __init__(self, mensagem="CPF inválido. Deve conter 11 dígitos numéricos."):
        super().__init__(mensagem)
