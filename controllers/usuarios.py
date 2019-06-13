"""."""
from .telaBase import Tela  # pylint: disable=relative-beyond-top-level
from .exibir import Exibir  # pylint: disable=relative-beyond-top-level
from models.usuario import Usuario  # pylint: disable=import-error


class Usuarios(Tela):
    """."""

    def on_pre_enter(self, *args, **kwargs):
        """."""
        super().on_pre_enter()
        self.ids.box.clear_widgets()
        usuarios = Usuario().select("SELECT nome FROM usuario", sel='fetchall')
        for i in usuarios:
            ex = Exibir()
            ex.texto = i.nome
            self.ids.box.add_widget(ex)


class UsuariosCadastrar(Tela):
    """."""

    ...
