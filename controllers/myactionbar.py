"""."""
from kivy.uix.actionbar import ActionBar
from kivy.properties import BooleanProperty, Property  # pylint: disable=no-name-in-module
from kivy.app import App


class MyActionBar(ActionBar):
    """."""

    prev = BooleanProperty(False)
    func = Property(lambda: ...)

    def __init__(self, *args, **kwargs):
        """."""
        super().__init__(*args, **kwargs)

    def usuario(self, args):
        """."""
        if args[1] != 'Usuarios':
            root = App.get_running_app().root
            root.current = args[1].replace(' ', '')+"usuarios"
            self.ids.usuarios.text = 'Usuarios'
            if root.current == 'Cadastrarusuarios':
                root.current_screen.ids.nome.text = ''
                root.current_screen.ids.email.text = ''
                root.current_screen.ids.cpf.text = ''
                root.current_screen.ids.telefone.text = ''
                root.current_screen.ids.senha.text = ''
                root.current_screen.ids.bib.active = False
                root.current_screen.ids.user.active = True
                root.current_screen.ids.nomeBotao.text = "Cadastrar"
