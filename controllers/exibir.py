"""."""
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import Property, StringProperty  # pylint: disable=no-name-in-module


class Exibir(BoxLayout):
    """."""

    texto = StringProperty()
    att = Property(lambda x: ...)
    deletar = Property(lambda x: ...)
