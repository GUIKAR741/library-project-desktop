"""Modulo com o Model Emprestimo."""
from . import Model


class Emprestimo(Model):
    """Model da Tabela Emprestimo."""

    def __init__(self, lista: dict = {}):
        """Inicia o Model."""
        super().__init__(lista)
        self.__table__ = 'emprestimo'
        self.__pk__ = 'id'
