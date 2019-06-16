"""."""
from kivy.app import App
from kivy.metrics import sp
from kivy.properties import (  # pylint: disable=no-name-in-module
    BooleanProperty, Property)
from kivy.uix.actionbar import ActionBar
from kivy.uix.button import Button

from .popuperror import PopupError  # pylint: disable=relative-beyond-top-level


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
            else:
                root.current_screen.on_pre_enter()

    def sair(self):
        """."""
        p = PopupError()
        p.titulo = "Deseja Realmente Sair?"
        p.size_hint_y = .2
        p.ids.box.clear_widgets()
        sim = Button(text='sim')
        sim.size_hint_y = None
        sim.height = sp(40)
        sim.on_release = (lambda: self._sair_func(p))
        nao = Button(text='não')
        nao.size_hint_y = None
        nao.height = sp(40)
        nao.on_release = p.dismiss
        p.ids.box.orientation = 'horizontal'
        p.ids.box.add_widget(sim)
        p.ids.box.add_widget(nao)
        p.open()

    def _sair_func(self, p):
        """."""
        p.dismiss()
        root = App.get_running_app().root
        root.current = 'login'
        root.current_screen.ids.email.text = ''
        root.current_screen.ids.senha.text = ''
