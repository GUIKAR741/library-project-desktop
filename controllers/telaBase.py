"""."""
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen


class Tela(Screen):
    """."""

    def funcao(self):
        """."""
        App.get_running_app().root.current = "menu"

    def voltar(self, window, key, *args):
        """."""
        if key == 27:
            App.get_running_app().root.current = 'menu'
            return True

    def on_pre_enter(self):
        """."""
        Window.bind(on_keyboard=self.voltar)

    def on_pre_leave(self):
        """."""
        Window.unbind(on_keyboard=self.voltar)
