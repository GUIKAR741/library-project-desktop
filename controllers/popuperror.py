"""Controller do Popup de Erro."""
from kivy.properties import Property  # pylint: disable=no-name-in-module
from kivy.properties import StringProperty  # pylint: disable=no-name-in-module
from kivy.uix.popup import Popup


class PopupError(Popup):
    """Componente Popup."""

    textoBotao = StringProperty('Fechar')

    titulo = StringProperty('')
    texto = StringProperty('')
    funcao = Property(lambda x: x.dismiss())
