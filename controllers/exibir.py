"""Controller do Componente Exibir."""
from kivy.properties import Property  # pylint: disable=no-name-in-module
from kivy.properties import StringProperty  # pylint: disable=no-name-in-module
from kivy.uix.boxlayout import BoxLayout


class Exibir(BoxLayout):
    """Componente Exibir."""

    textoBotaoAtualizar = StringProperty("Atualizar")
    textoBotaoExcluir = StringProperty("Excluir")

    texto = StringProperty()
    att = Property(lambda x: ...)
    deletar = Property(lambda x: ...)
