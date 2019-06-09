"""."""
from . import Model


class Emprestimo(Model):
    """."""

    def __init__(self, lista: dict = {}):
        """."""
        super().__init__(lista)
        self.__table__ = 'emprestimo'
        self.__pk__ = 'id'
