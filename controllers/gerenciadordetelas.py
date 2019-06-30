"""Controller do Gerenciador de Telas."""
from kivy.uix.screenmanager import FadeTransition, ScreenManager


class GerenciadorDeTelas(ScreenManager):
    """Componente Gerenciador de Telas."""

    def __init__(self, *args, **kwargs):
        """Inicializador do Objeto."""
        super().__init__(*args, **kwargs)
        self.transition = FadeTransition()
