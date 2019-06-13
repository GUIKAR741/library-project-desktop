"""."""
import kivy
from kivy.app import App
from controllers.myactionbar import MyActionBar  # pylint: disable=unused-import
from controllers.exibir import Exibir  # pylint: disable=unused-import
from controllers.gerenciadordetelas import GerenciadorDeTelas  # pylint: disable=unused-import
from controllers.menu import Menu  # pylint: disable=unused-import
from controllers.usuarios import Usuarios, UsuariosCadastrar  # pylint: disable=unused-import
from controllers.acervo import (  # pylint: disable=unused-import
    Livros,
    LivrosCadastrar,
    Exemplares,
    ExemplaresCadastrar
    )
from controllers.reservas import Reservas  # pylint: disable=unused-import
from controllers.emprestimos import (  # pylint: disable=unused-import
    Emprestimos,
    Devolucoes,
    Emprestar
    )
kivy.require("1.11.0")


class Main(App):
    """."""

    def build(self):
        """."""
        self.icon = "res/icon.png"
        self.title = "SYML"
        super().build()

Main().run()
