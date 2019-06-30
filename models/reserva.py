"""Modulo com o Model Reserva."""
from . import Model


class Reserva(Model):
    """Model da Tabela Reserva."""

    def __init__(self, lista: dict = {}):
        """Inicia o Model."""
        super().__init__(lista)
        self.__table__ = 'reserva'
        self.__pk__ = 'id'
