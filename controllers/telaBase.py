"""Tela Base Para outras Telas."""
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen


class Tela(Screen):
    """Tela Base."""

    def funcao(self):
        """Função do Botão Voltar da Action Bar."""
        App.get_running_app().root.current = "menu"

    def voltar(self, window, key, *args):
        """Função Bind para Voltar."""
        if key == 27:
            App.get_running_app().root.current = 'menu'
            return True

    def on_pre_enter(self):
        """Executa antes de Entrar na Tela."""
        Window.bind(on_keyboard=self.voltar)

    def on_pre_leave(self):
        """Executa ao sair de uma Tela."""
        Window.unbind(on_keyboard=self.voltar)
