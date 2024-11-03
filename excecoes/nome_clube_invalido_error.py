class NomeClubeInvalidoError(Exception):
    def __init__(self, mensagem="O nome do clube é inválido. Ele não pode estar vazio."):
        super().__init__(mensagem)
