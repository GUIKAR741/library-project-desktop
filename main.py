"""."""
import kivy
from kivy.app import App

from controllers.acervo import (Exemplares,  # pylint: disable=unused-import
                                ExemplaresCadastrar, Livros, LivrosCadastrar)
from controllers.emprestimos import (  # pylint: disable=unused-import
    Devolucoes, Emprestar, Emprestimos)
from controllers.exibir import Exibir  # pylint: disable=unused-import
from controllers.gerenciadordetelas import (  # pylint: disable=unused-import
    GerenciadorDeTelas
)
from controllers.login import Login  # pylint: disable=unused-import
from controllers.menu import Menu  # pylint: disable=unused-import
from controllers.myactionbar import (  # pylint: disable=unused-import
    MyActionBar
)
from controllers.popuperror import PopupError  # pylint: disable=unused-import
from controllers.reservas import Reservas  # pylint: disable=unused-import
from controllers.usuarios import (Usuarios,  # pylint: disable=unused-import
                                  UsuariosCadastrar)

# from kivy.lang import Builder


kivy.require("1.11.0")


class Main(App):
    """."""

    def build(self):
        """."""
        self.icon = "res/icon.png"
        self.title = "SYML"
        super().build()
        # with open("main.kv", encoding='utf8') as f:
        #     Builder.load_string(f.read())


Main().run()
