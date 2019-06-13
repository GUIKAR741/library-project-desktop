"""."""
from .telaBase import Tela  # pylint: disable=relative-beyond-top-level
from .exibir import Exibir  # pylint: disable=relative-beyond-top-level
from kivy.metrics import sp
from models.reserva import Reserva  # pylint: disable=import-error


class Reservas(Tela):
    """."""

    def on_pre_enter(self, *args, **kwargs):
        """."""
        super().on_pre_enter()
        self.ids.box.clear_widgets()
        livros = Reserva().select(
            """SELECT u.nome, l.titulo, r.data FROM reserva r
            join livro l on r.livro_id=l.id
            join usuario u on u.id = r.usuario_id
            WHERE status = 1""", sel='fetchall')
        for i in livros:
            ex = Exibir()
            ex.height = sp(70)
            ex.texto = "Usuario: " + i.nome + \
                       "\nTitulo: " + i.titulo + \
                       "\nData: " + i.data.strftime("%d/%m/%Y")
            self.ids.box.add_widget(ex)
