"""."""
from kivy.animation import Animation
from kivy.app import App
from kivy.core.window import Window
from kivy.properties import StringProperty  # pylint: disable=no-name-in-module
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import Screen

from models.usuario import Usuario  # pylint: disable=import-error

from .popuperror import PopupError  # pylint: disable=relative-beyond-top-level


class Login(Screen):
    """."""

    textoEmail = StringProperty('Email:')
    textoSenha = StringProperty('Senha:')
    textoBotaoLogin = StringProperty('Logar')

    email = StringProperty('')
    senha = StringProperty('')

    def fazerLogin(self):
        """."""
        p = PopupError()
        p.titulo = "Erro ao Logar!"
        p.texto = ""
        usuario = Usuario().procurarUsuarioPeloEmail(self.ids.email.text)
        if usuario:
            if usuario.verify_password('senha', self.ids.senha.text):
                if usuario.tipo == 1:
                    p.titulo = "Logado com Sucesso!"
                    p.texto += 'Bem Vindo ao SYML!'
                    p.open()
                    runApp = App.get_running_app()
                    runApp.root.idUsuario = usuario.id
                    runApp.root.current = 'menu'
                else:
                    p.texto += 'Usuario Não É Bibliotecário!'
                    p.open()
            else:
                p.texto += 'Senha Incorreta!'
                p.open()
        else:
            p.texto += 'Usuario Não Existe!'
            p.open()

    def on_pre_enter(self):
        """."""
        Window.bind(on_request_close=self.confirmacao)

    def confirmacao(self, *args, **kwargs):
        """."""
        box = BoxLayout(orientation='vertical', padding=10, spacing=10)
        botoes = BoxLayout(padding=10, spacing=10)

        pop = Popup(title='Deseja mesmo sair?', content=box, size_hint=(None, None),
                    size=(200, 200))

        sim = Button(text='Sim', on_release=App.get_running_app().stop)
        nao = Button(text='Não', on_release=pop.dismiss)

        botoes.add_widget(sim)
        botoes.add_widget(nao)

        atencao = Image(source='res/atencao.png')

        box.add_widget(atencao)
        box.add_widget(botoes)

        animText = Animation(color=(0, 0, 0, 1)) + \
            Animation(color=(1, 1, 1, 1))
        animText.repeat = True
        animText.start(sim)
        anim = Animation(size=(300, 180), duration=0.2, t='out_back')
        anim.start(pop)
        pop.open()
        return True
