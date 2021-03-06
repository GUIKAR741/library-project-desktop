"""Controller Componente MyActionBar."""
from kivy.app import App
from kivy.metrics import sp
from kivy.properties import (  # pylint: disable=no-name-in-module
    BooleanProperty, ListProperty, Property, StringProperty)
from kivy.uix.actionbar import ActionBar
from kivy.uix.button import Button

from .popuperror import PopupError  # pylint: disable=relative-beyond-top-level


class MyActionBar(ActionBar):
    """Customização da ActionBar."""

    textoLogo = StringProperty("SYML")
    textoUsuarios = StringProperty("Usuarios")
    textoAcervo = StringProperty("Acervo")
    textoReservas = StringProperty("Reservas")
    textoEmprestimos = StringProperty("Emprestimos")
    textoSair = StringProperty("Sair")

    listaOpcoesUsuarios = ListProperty(['Ver Todos', 'Cadastrar'])
    listaOpcoesAcervo = ListProperty(
        ['Livros', 'Exemplares', 'Cadastrar Livro', 'Cadastrar Exemplar'])
    listaOpcoesReservas = ListProperty(['Ver Todas'])
    listaOpcoesEmprestimos = ListProperty(
        ['Ver Todos', "Devoluções", "Emprestar Livro"])

    prev = BooleanProperty(False)
    func = Property(lambda: ...)

    def usuario(self, args):
        """Função para escolher opção do botão Usuario."""
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

    def acervo(self, args):
        """Função para escolher opção do botão Acervo."""
        if args[1] != 'Acervo':
            root = App.get_running_app().root
            root.current = args[1].replace(' ', '')+"acervo"
            self.ids.acervo.text = 'Acervo'
            root.current_screen.on_pre_enter()

    def reserva(self, args):
        """Função para escolher opção do botão Reserva."""
        if args[1] != 'Reservas':
            root = App.get_running_app().root
            root.current = args[1].replace(' ', '')+"reservas"
            self.ids.reservas.text = 'Reservas'
            root.current_screen.on_pre_enter()

    def emprestimo(self, args):
        """Função para escolher opção do botão Emprestimo."""
        if args[1] != 'Emprestimos':
            root = App.get_running_app().root
            root.current = args[1].replace(' ', '')+"emprestimos"
            self.ids.emprestimos.text = 'Emprestimos'
            root.current_screen.on_pre_enter()

    def sair(self):
        """Função para Sair do Aplicativo."""
        p = PopupError()
        p.titulo = "Deseja Realmente Sair?"
        p.size_hint_y = .2
        p.ids.box.clear_widgets()
        sim = Button(text='sim')
        sim.size_hint_y = None
        sim.height = sp(40)
        sim.on_release = (lambda: self._sair_func(p))
        sim.background_color = (
            0.1607843137254902,
            0.7137254901960784,
            0.9647058823529412,
            1
        )
        nao = Button(text='não')
        nao.size_hint_y = None
        nao.height = sp(40)
        nao.on_release = p.dismiss
        nao.background_color = (
            0.1607843137254902,
            0.7137254901960784,
            0.9647058823529412,
            1
        )
        p.ids.box.orientation = 'horizontal'
        p.ids.box.add_widget(sim)
        p.ids.box.add_widget(nao)
        p.open()

    def _sair_func(self, p):
        """Função Auxiliar para Sair."""
        p.dismiss()
        root = App.get_running_app().root
        root.current = 'login'
        root.current_screen.ids.email.text = ''
        root.current_screen.ids.senha.text = ''
