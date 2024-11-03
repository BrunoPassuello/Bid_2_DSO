class SalarioInvalidoError(Exception):
    def __init__(self, mensagem="Salário inválido. Deve ser um número positivo."):
        super().__init__(mensagem)
