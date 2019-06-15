"""."""
from kivy.uix.popup import Popup
from kivy.properties import StringProperty, Property  # pylint: disable=no-name-in-module


class PopupError(Popup):
    """."""

    titulo = StringProperty('')
    texto = StringProperty('')
    funcao = Property(lambda x: x.dismiss())
