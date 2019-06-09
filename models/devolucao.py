"""."""
from . import Model


class Devolucao(Model):
    """."""

    def __init__(self, lista: dict = {}):
        """."""
        super().__init__(lista)
        self.__table__ = 'devolucao'
        self.__pk__ = 'id'
