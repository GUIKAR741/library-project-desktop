"""."""
from . import Model


class Exemplar(Model):
    """."""

    def __init__(self, lista: dict = {}):
        """."""
        super().__init__(lista)
        self.__table__ = 'exemplar'
        self.__pk__ = 'id'
