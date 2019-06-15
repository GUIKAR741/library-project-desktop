"""."""
from kivy.properties import StringProperty, BooleanProperty  # pylint: disable=no-name-in-module
from kivy.app import App
from kivy.clock import Clock
from .telaBase import Tela  # pylint: disable=relative-beyond-top-level
from .exibir import Exibir  # pylint: disable=relative-beyond-top-level
from .popuperror import PopupError  # pylint: disable=relative-beyond-top-level
from models.usuario import Usuario  # pylint: disable=import-error


class Usuarios(Tela):
    """."""

    def on_pre_enter(self, *args, **kwargs):
        """."""
        super().on_pre_enter()
        self.ids.box.clear_widgets()
        Clock.schedule_once(self.addUsuarios, .5)

    def addUsuarios(self, dt):
        """."""
        usuarios = Usuario().select("SELECT nome FROM usuario", sel='fetchall')
        for i in usuarios:
            ex = Exibir()
            ex.texto = i.nome
            self.ids.box.add_widget(ex)


class UsuariosCadastrar(Tela):
    """."""

    nomeBotao = StringProperty('Cadastrar')
    nome = StringProperty('')
    email = StringProperty('')
    cpf = StringProperty('')
    telefone = StringProperty('')
    senha = StringProperty('')
    bib = BooleanProperty(False)
    user = BooleanProperty(True)

    def on_pre_enter(self):
        """."""
        super().on_pre_enter()
        self.ids.cpf.bind(text=self.cpf_val)
        self.ids.telefone.bind(text=self.telefone_val)

    def val_form(self):
        """."""
        u = Usuario()
        u.nome = self.ids.nome.text
        filemail = list(filter(lambda x: x == '@' or x == '.', self.ids.email.text))
        u.email = self.ids.email.text
        u.telefone = self.ids.telefone.text
        u.cpf = ''.join(
            list(filter(lambda z: z.isdigit(),
                        self.ids.cpf.text)))
        u.senha = self.ids.senha.text
        u.tipo = 1 if self.ids.bib.active else 0
        p = PopupError()
        err = 0
        p.texto = ''
        if not ('@' in filemail and '.' in filemail):
            p.texto += "Email Invalido.\n"
            err += 1
        if len(u.telefone) < 14:
            p.texto += "Telefone Invalido.\n"
            err += 1
        if len(u.cpf) < 11:
            p.texto += "CPF Invalido.\n"
            err += 1
        if err > 0:
            p.titulo = "Erro!"
            p.open()
        else:
            p.titulo = 'Sucesso!'
            p.texto = 'Cadastrado Com Sucesso!'
            p.funcao = self._mudaAoTerminar
            u.criptografar_senha('senha')
            u.insert()
            p.open()

    def _mudaAoTerminar(self, instancia):
        App.get_running_app().root.current = 'VerTodosusuarios'
        instancia.dismiss()

    def cpf_val(self, ins, val):
        """."""
        txt = ''.join(
            list(filter(lambda z: z.isdigit(), ins.text))[:11])
        texto = ''
        for i in range(len(txt)):
            if i == 3:
                texto += '.'
                texto += txt[i]
                continue
            if i == 6:
                texto += '.'
                texto += txt[i]
                continue
            if i == 9:
                texto += '-'
                texto += txt[i]
                continue
            texto += txt[i]
        ins.text = texto

    def telefone_val(self, ins, val):
        """."""
        txt = ''.join(
            list(filter(lambda z: z.isdigit(), ins.text))[:11])
        texto = ''
        for i in range(len(txt)):
            if i == 0:
                texto += '('
                texto += txt[i]
                continue
            if i == 2:
                texto += ')'
                texto += txt[i]
                continue
            if i == 6:
                texto += txt[i]
                texto += '-'
                continue
            texto += txt[i]
        ins.text = texto
