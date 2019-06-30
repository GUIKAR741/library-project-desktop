"""Modulo com o Model Livro."""
from . import Model


class Livro(Model):
    """Model da Tabela Livro."""

    def __init__(self, lista: dict = {}):
        """Inicia o Model."""
        super().__init__(lista)
        self.__table__ = 'livro'
        self.__pk__ = 'id'
