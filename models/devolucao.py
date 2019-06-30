"""Modulo com o Model Devolucao."""
from . import Model


class Devolucao(Model):
    """Model da Tabela Devolucao."""

    def __init__(self, lista: dict = {}):
        """Inicia o Model."""
        super().__init__(lista)
        self.__table__ = 'devolucao'
        self.__pk__ = 'id'
