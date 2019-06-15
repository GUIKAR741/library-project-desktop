"""."""
import kivy
from kivy.app import App
# from kivy.lang import Builder

from controllers.acervo import (  # pylint: disable=unused-import
    Exemplares,
    ExemplaresCadastrar,
    Livros,
    LivrosCadastrar
)
from controllers.emprestimos import (  # pylint: disable=unused-import
    Devolucoes,
    Emprestar,
    Emprestimos
)
from controllers.exibir import Exibir  # pylint: disable=unused-import
from controllers.popuperror import PopupError  # pylint: disable=unused-import
from controllers.gerenciadordetelas import (  # pylint: disable=unused-import
    GerenciadorDeTelas
)
from controllers.menu import Menu  # pylint: disable=unused-import
from controllers.myactionbar import (  # pylint: disable=unused-import
    MyActionBar
)
from controllers.reservas import Reservas  # pylint: disable=unused-import
from controllers.usuarios import (  # pylint: disable=unused-import
    Usuarios,
    UsuariosCadastrar
)

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
