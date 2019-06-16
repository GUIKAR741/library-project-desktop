"""."""
from kivy.clock import Clock
from kivy.metrics import sp

from models.exemplar import Exemplar  # pylint: disable=import-error
from models.livro import Livro  # pylint: disable=import-error

from .exibir import Exibir  # pylint: disable=relative-beyond-top-level
from .telaBase import Tela  # pylint: disable=relative-beyond-top-level


class Livros(Tela):
    """."""

    def on_pre_enter(self, *args, **kwargs):
        """."""
        super().on_pre_enter()
        Clock.schedule_once(self.addLivro, .5)

    def addLivro(self, dt):
        """."""
        self.ids.box.clear_widgets()
        livros = Livro().select("SELECT titulo, autor FROM livro", sel='fetchall')
        if len(livros) > 0:
            for i in livros:
                ex = Exibir()
                ex.height = sp(50)
                ex.texto = (f"Titulo: {i.titulo}\n"
                            f"Autor: {i.autor}")
                self.ids.box.add_widget(ex)
        else:
            ex = Exibir()
            ex.remove_widget(ex.ids.att)
            ex.remove_widget(ex.ids.deletar)
            ex.height = sp(50)
            ex.ids.texto.font_size = sp(20)
            ex.texto = "Não há Livros!"
            self.ids.box.add_widget(ex)


class LivrosCadastrar(Tela):
    """."""

    ...


class Exemplares(Tela):
    """."""

    def on_pre_enter(self, *args, **kwargs):
        """."""
        super().on_pre_enter()
        Clock.schedule_once(self.addEx, .5)

    def addEx(self, dt):
        """."""
        self.ids.box.clear_widgets()
        livros = Exemplar().select(
            "SELECT l.titulo, e.codigo FROM livro l JOIN exemplar e ON l.id=e.livro_id",
            sel='fetchall'
        )
        if len(livros) > 0:
            for i in livros:
                ex = Exibir()
                ex.texto = "Titulo: " + i.titulo + '\n' + \
                           "Codigo: " + i.codigo
                ex.height = sp(130)
                self.ids.box.add_widget(ex)
        else:
            ex = Exibir()
            ex.remove_widget(ex.ids.att)
            ex.remove_widget(ex.ids.deletar)
            ex.height = sp(50)
            ex.ids.texto.font_size = sp(20)
            ex.texto = "Não há Exemplares!"
            self.ids.box.add_widget(ex)


class ExemplaresCadastrar(Tela):
    """."""

    ...
