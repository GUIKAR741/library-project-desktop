"""."""
from kivy.app import App
from kivy.clock import Clock
from kivy.metrics import sp
from kivy.properties import (  # pylint: disable=no-name-in-module
    BooleanProperty, StringProperty)
from kivy.uix.button import Button

from models.usuario import Usuario  # pylint: disable=import-error

from .exibir import Exibir  # pylint: disable=relative-beyond-top-level
from .popuperror import PopupError  # pylint: disable=relative-beyond-top-level
from .telaBase import Tela  # pylint: disable=relative-beyond-top-level


class Usuarios(Tela):
    """."""

    def on_pre_enter(self, *args, **kwargs):
        """."""
        super().on_pre_enter()
        Clock.schedule_once(self.addUsuarios, .5)

    def addUsuarios(self, dt):
        """."""
        self.ids.box.clear_widgets()
        usuarios = Usuario().select(
            """
            SELECT id, nome, email, tipo
            FROM usuario
            """,
            sel='fetchall'
        )
        if len(usuarios) > 0:
            for i in usuarios:
                ex = Exibir()
                ex.idUser = i.id
                ex.att = self.atualizar
                ex.deletar = self.deletar
                ex.height = sp(70)
                ex.texto = (f"Nome: {i.nome}\n"
                            f"Email: {i.email}\n"
                            f"Tipo: {'Bibliotecário' if i.tipo==1 else 'Usuario'}")
                self.ids.box.add_widget(ex)
        else:
            ex = Exibir()
            ex.remove_widget(ex.ids.att)
            ex.remove_widget(ex.ids.deletar)
            ex.height = sp(50)
            ex.ids.texto.font_size = sp(20)
            ex.texto = "Não há Usuarios!"
            self.ids.box.add_widget(ex)

    def atualizar(self, instancia):
        """."""
        user = Usuario().select(
            "SELECT * FROM usuario WHERE id = %(id)s",
            {'id': instancia.idUser}
        )
        root = App.get_running_app().root
        root.current = 'Cadastrarusuarios'
        root.current_screen.idUser = user.id
        root.current_screen.ids.nome.text = user.nome
        root.current_screen.ids.email.text = user.email
        root.current_screen.ids.cpf.text = user.cpf
        root.current_screen.ids.telefone.text = user.telefone
        root.current_screen.ids.senha.text = ''
        root.current_screen.ids.bib.active = True if user.tipo == 1 else False
        root.current_screen.ids.user.active = True if user.tipo == 0 else False
        root.current_screen.ids.nomeBotao.text = "Atualizar"

    def deletar(self, instancia):
        """."""
        p = PopupError()
        p.titulo = "Deseja Realmente Excluir?"
        p.size_hint_y = .2
        p.ids.box.clear_widgets()
        sim = Button(text='sim')
        sim.size_hint_y = None
        sim.height = sp(40)
        sim.on_release = (lambda: self.del_troca(instancia, p))
        nao = Button(text='não')
        nao.size_hint_y = None
        nao.height = sp(40)
        nao.on_release = p.dismiss
        p.ids.box.orientation = 'horizontal'
        p.ids.box.add_widget(sim)
        p.ids.box.add_widget(nao)
        p.open()

    def del_troca(self, ins, popup):
        """."""
        popup.dismiss()
        Usuario().delete('id', ins.idUser)
        App.get_running_app().root.current_screen.on_pre_enter()


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
        filemail = list(filter(lambda x: x == '@' or x ==
                               '.', self.ids.email.text))
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
        if len(filemail) < 2:
            p.texto += "Email Invalido.\n"
            err += 1
        if err != 1 and not ('@' in filemail and '.' == filemail[-1]):
            p.texto += "Email Invalido.\n"
            err += 1
        if len(u.telefone) < 14:
            p.texto += "Telefone Invalido.\n"
            err += 1
        if len(u.senha) < 1:
            p.texto += "Senha Invalida.\n"
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
            if self.ids.nomeBotao.text == 'Cadastrar':
                u.insert()
            else:
                p.texto = 'Atualizado Com Sucesso!'
                u.update('id', self.idUser)
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
