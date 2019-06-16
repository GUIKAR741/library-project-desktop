"""."""
from kivy.properties import StringProperty  # pylint: disable=no-name-in-module
from kivy.uix.screenmanager import Screen

from models.emprestimo import Emprestimo  # pylint: disable=import-error


class Menu(Screen):
    """."""

    emprestimos = StringProperty()
    reservas = StringProperty()
    livros = StringProperty()
    usuarios = StringProperty()

    def __init__(self, *args, **kwargs):
        """."""
        super().__init__(*args, **kwargs)

        total = Emprestimo().select("SELECT count(id) as usr FROM usuario")
        self.usuarios = "[size=20]Usuarios\n[/size]" + \
            str(total.usr) + " Usuarios Cadastrados"

        total = Emprestimo().select("SELECT count(id) as liv FROM livro")
        self.livros = "[size=20]Livros\n[/size]" + \
            str(total.liv) + " Livros Cadastrados"

        total = Emprestimo().select("SELECT count(id) as ex FROM exemplar")
        self.exemplares = "[size=20]Exemplares\n[/size]" + \
            str(total.ex) + " Exemplares Cadastrados"

        total = Emprestimo().select("SELECT count(id) as emp FROM emprestimo")
        self.emprestimos = "[size=20]Empréstimos\n[/size]" + \
            str(total.emp) + " Empréstimos Realizados"

        total = Emprestimo().select("SELECT count(id) as dev FROM devolucao")
        self.devolucoes = "[size=20]Devoluções\n[/size]" + \
            str(total.dev) + " Devoluções Realizadas"

        total = Emprestimo().select("SELECT count(id) as res FROM reserva")
        self.reservas = "[size=20]Reservas\n[/size]" + \
            str(total.res) + " Reservas Realizadas"
