"""."""
from kivy.metrics import sp
from .telaBase import Tela  # pylint: disable=relative-beyond-top-level
from .exibir import Exibir  # pylint: disable=relative-beyond-top-level
from models.livro import Livro  # pylint: disable=import-error
from models.exemplar import Exemplar  # pylint: disable=import-error
from kivy.clock import Clock


class Livros(Tela):
    """."""

    def on_pre_enter(self, *args, **kwargs):
        """."""
        super().on_pre_enter()
        self.ids.box.clear_widgets()
        Clock.schedule_once(self.addLivro, .5)

    def addLivro(self, dt):
        """."""
        livros = Livro().select("SELECT titulo FROM livro", sel='fetchall')
        for i in livros:
            ex = Exibir()
            ex.texto = i.titulo
            self.ids.box.add_widget(ex)


class LivrosCadastrar(Tela):
    """."""

    ...


class Exemplares(Tela):
    """."""

    def on_pre_enter(self, *args, **kwargs):
        """."""
        super().on_pre_enter()
        self.ids.box.clear_widgets()
        Clock.schedule_once(self.addEx, .5)

    def addEx(self, dt):
        """."""
        livros = Exemplar().select(
            "SELECT l.titulo, e.codigo FROM livro l JOIN exemplar e ON l.id=e.livro_id",
            sel='fetchall'
        )
        for i in livros:
            ex = Exibir()
            ex.texto = "Titulo: " + i.titulo + '\n' + \
                       "Codigo: " + i.codigo
            ex.height = sp(130)
            self.ids.box.add_widget(ex)


class ExemplaresCadastrar(Tela):
    """."""

    ...
