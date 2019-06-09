"""."""
from . import Model


class Reserva(Model):
    """."""

    def __init__(self, lista: dict = {}):
        """."""
        super().__init__(lista)
        self.__table__ = 'reserva'
        self.__pk__ = 'id'
