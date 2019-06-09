"""."""
from . import Model


class Livro(Model):
    """."""

    def __init__(self, lista: dict = {}):
        """."""
        super().__init__(lista)
        self.__table__ = 'livro'
        self.__pk__ = 'id'
