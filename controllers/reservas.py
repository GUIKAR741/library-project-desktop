"""."""
from kivy.uix.screenmanager import Screen
from kivy.app import App
from kivy.properties import StringProperty  # pylint: disable=no-name-in-module
from models.emprestimo import Emprestimo  # pylint: disable=import-error


class Reservas(Screen):
    """."""

    def __init__(self, *args, **kwargs):
        """."""
        super().__init__(*args, **kwargs)

    def funcao(self):
        """."""
        App.get_running_app().root.current = "menu"
