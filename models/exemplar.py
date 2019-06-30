"""Modulo com o Model Exemplar."""
from . import Model


class Exemplar(Model):
    """Model da Tabela Exemplar."""

    def __init__(self, lista: dict = {}):
        """Inicia o Model."""
        super().__init__(lista)
        self.__table__ = 'exemplar'
        self.__pk__ = 'id'
