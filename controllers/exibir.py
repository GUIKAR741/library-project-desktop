"""."""
from kivy.properties import (Property,  # pylint: disable=no-name-in-module
                             StringProperty)
from kivy.uix.boxlayout import BoxLayout


class Exibir(BoxLayout):
    """."""

    texto = StringProperty()
    att = Property(lambda x: ...)
    deletar = Property(lambda x: ...)
