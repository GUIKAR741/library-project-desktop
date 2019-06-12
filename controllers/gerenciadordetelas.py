"""."""
from kivy.uix.screenmanager import ScreenManager, FadeTransition


class GerenciadorDeTelas(ScreenManager):
    """."""

    def __init__(self, *args, **kwargs):
        """."""
        super().__init__(*args, **kwargs)
        self.transition = FadeTransition()
