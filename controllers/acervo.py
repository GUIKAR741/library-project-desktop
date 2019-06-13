"""."""
from kivy.properties import Property, StringProperty  # pylint: disable=no-name-in-module
from kivy.uix.boxlayout import BoxLayout
from .telaBase import Tela  # pylint: disable=relative-beyond-top-level
from .exibir import Exibir  # pylint: disable=relative-beyond-top-level
from models.livro import Livro  # pylint: disable=import-error
from models.exemplar import Exemplar  # pylint: disable=import-error


class ExibirExemplar(BoxLayout):
    """."""

    livro = StringProperty()
    ex = StringProperty()
    att = Property(lambda: ...)
    deletar = Property(lambda: ...)


class Livros(Tela):
    """."""

    def on_pre_enter(self, *args, **kwargs):
        """."""
        super().on_pre_enter()
        self.ids.box.clear_widgets()
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
        livros = Exemplar().select(
            "SELECT l.titulo, e.codigo FROM livro l JOIN exemplar e ON l.id=e.livro_id",
            sel='fetchall'
            )
        for i in livros:
            ex = ExibirExemplar()
            ex.livro = i.titulo[:30]+'...'
            ex.ex = i.codigo
            self.ids.box.add_widget(ex)


class ExemplaresCadastrar(Tela):
    """."""

    ...
