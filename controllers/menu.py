"""."""
from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty  # pylint: disable=no-name-in-module
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
        total = Emprestimo().select("SELECT count(id) as emp FROM emprestimo")
        self.emprestimos = "Emprestimos\n" + \
            str(total.emp) + " Emprestimos Realizados"
        total = Emprestimo().select("SELECT count(id) as res FROM reserva")
        self.reservas = "Reservas\n" + \
            str(total.res) + " Reservas Realizadas"
        total = Emprestimo().select("SELECT count(id) as liv FROM livro")
        totalex = Emprestimo().select("SELECT count(id) as ex FROM exemplar")
        self.livros = "Livros\n" + \
            str(total.liv) + " Livros Cadastrados\n\n" + \
            "Exemplares\n" + \
            str(totalex.ex) + " Exemplares Cadastrados"
        total = Emprestimo().select("SELECT count(id) as usr FROM usuario")
        self.usuarios = "Usuarios\n" + \
            str(total.usr) + " Usuarios Cadastrados"
