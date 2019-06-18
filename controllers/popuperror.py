"""."""
from kivy.properties import (Property,  # pylint: disable=no-name-in-module
                             StringProperty)
from kivy.uix.popup import Popup


class PopupError(Popup):
    """."""

    textoBotao = StringProperty('Fechar')

    titulo = StringProperty('')
    texto = StringProperty('')
    funcao = Property(lambda x: x.dismiss())
