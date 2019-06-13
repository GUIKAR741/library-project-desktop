"""."""
from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty  # pylint: disable=no-name-in-module
from models.emprestimo import Emprestimo  # pylint: disable=import-error
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.animation import Animation


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
