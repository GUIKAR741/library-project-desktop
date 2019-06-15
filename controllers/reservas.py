"""."""
from kivy.metrics import sp
from kivy.clock import Clock
from kivy.uix.button import Button

from models.reserva import Reserva  # pylint: disable=import-error

from .exibir import Exibir  # pylint: disable=relative-beyond-top-level
from .telaBase import Tela  # pylint: disable=relative-beyond-top-level


class Reservas(Tela):
    """."""

    def on_pre_enter(self, *args, **kwargs):
        """."""
        super().on_pre_enter()
        self.ids.box.clear_widgets()
        Clock.schedule_once(self.addReservas, .5)

    def addReservas(self, dt):
        """."""
        livros = Reserva().select(
            """SELECT u.nome, l.titulo, r.data FROM reserva r
            join livro l on r.livro_id=l.id
            join usuario u on u.id = r.usuario_id
            WHERE status = 1 ORDER BY r.data desc""", sel='fetchall')
        for i in livros:
            ex = Exibir()
            text = list(filter(lambda x: type(x) is Button, ex.children))
            for j in range(len(text)):
                ex.remove_widget(text[j])
            ex.height = sp(70)
            ex.texto = "Usuario: " + i.nome + \
                       "\nTitulo: " + i.titulo + \
                       "\nData: " + i.data.strftime("%d/%m/%Y")
            self.ids.box.add_widget(ex)
