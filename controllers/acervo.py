"""."""
from kivy.clock import Clock
from kivy.metrics import sp
from kivy.app import App
from kivy.uix.button import Button
from kivy.properties import StringProperty  # pylint: disable=no-name-in-module

from models.exemplar import Exemplar  # pylint: disable=import-error
from models.livro import Livro  # pylint: disable=import-error

from .exibir import Exibir  # pylint: disable=relative-beyond-top-level
from .popuperror import PopupError  # pylint: disable=relative-beyond-top-level
from .telaBase import Tela  # pylint: disable=relative-beyond-top-level


class Livros(Tela):
    """."""

    def on_pre_enter(self, *args, **kwargs):
        """."""
        super().on_pre_enter()
        Clock.schedule_once(self.addLivro, .5)

    def addLivro(self, dt):
        """."""
        self.ids.box.clear_widgets()
        livros = Livro().select("SELECT id, titulo, autor FROM livro", sel='fetchall')
        if len(livros) > 0:
            for i in livros:
                ex = Exibir()
                ex.height = sp(50)
                ex.texto = (f"Titulo: {i.titulo}\n"
                            f"Autor: {i.autor}")
                ex.idL = i.id
                # ex.att = self.atualizar
                ex.deletar = self.deletar
                self.ids.box.add_widget(ex)
        else:
            ex = Exibir()
            ex.remove_widget(ex.ids.att)
            ex.remove_widget(ex.ids.deletar)
            ex.height = sp(50)
            ex.ids.texto.font_size = sp(20)
            ex.texto = "Não há Livros!"
            self.ids.box.add_widget(ex)

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
        Livro().delete('id', ins.idL)
        App.get_running_app().root.current_screen.on_pre_enter()


class LivrosCadastrar(Tela):
    """."""

    textoBotaoCadastrar = StringProperty("Cadastrar")

    textoLabelTitulo = StringProperty("Título:")
    textoLabelAutor = StringProperty("Autor:")
    textoLabelUrl = StringProperty("URL Capa:")
    textoLabelEditora = StringProperty("Editora:")
    textoLabelAno = StringProperty("Ano:")
    textoLabelIdioma = StringProperty("Idioma:")
    textoLabelISBN = StringProperty("ISBN:")
    textoLabelDescricao = StringProperty("Descrição:")

    textTitulo = StringProperty('')
    textAutor = StringProperty('')
    textUrl = StringProperty('')
    textEditora = StringProperty('')
    textAno = StringProperty('')
    textIdioma = StringProperty('')
    textISBN = StringProperty('')
    textDescricao = StringProperty('')

    def on_pre_enter(self, *args, **kwargs):
        """."""
        super().on_pre_enter()
        self.ids.titulo.text = ''
        self.ids.autor.text = ''
        self.ids.url.text = ''
        self.ids.ano.text = ''
        self.ids.idioma.text = ''
        self.ids.isbn.text = ''
        self.ids.descricao.text = ''

    def validaAno(self):
        """."""
        self.ids.ano.text = ''.join(
            list(
                filter(
                    lambda x: x.isdigit(),
                    self.ids.ano.text
                    )
                )
            )[:4]
        self.textAno = self.ids.ano.text

    def cadLivro(self):
        """."""
        p = PopupError()
        err = 0
        p.texto = ''
        if self.textTitulo == '':
            p.texto += "Digite um Titulo.\n"
            err += 1
        if self.textAutor == '':
            p.texto += "Digite o Autor.\n"
            err += 1
        if self.textUrl == '':
            p.texto += "Digite a URL.\n"
            err += 1
        if self.textEditora == '':
            p.texto += "Digite a Editora.\n"
            err += 1
        if self.textAno == '':
            p.texto += "Digite o Ano.\n"
            err += 1
        if self.textIdioma == '':
            p.texto += "Digite o Idioma.\n"
            err += 1
        if self.textISBN == '':
            p.texto += "Digite o ISBN.\n"
            err += 1
        if self.textDescricao == '':
            p.texto += "Digite a Descrição.\n"
            err += 1
        if err > 0:
            p.titulo = "Erro!"
            p.open()
        else:
            p.titulo = 'Sucesso!'
            p.texto = 'Cadastrado Com Sucesso!'
            p.funcao = self._mudaAoTerminar
            e = Livro()
            e.titulo = self.textTitulo
            e.autor = self.textAutor
            e.editora = self.textEditora
            e.capa = self.textUrl
            e.ano = self.textAno
            e.idioma = self.textIdioma
            e.isbn = self.textISBN
            e.descricao = self.textDescricao
            e.insert()
            p.open()

    def _mudaAoTerminar(self, instancia):
        """."""
        App.get_running_app().root.current = 'Livrosacervo'
        instancia.dismiss()


class Exemplares(Tela):
    """."""

    def on_pre_enter(self, *args, **kwargs):
        """."""
        super().on_pre_enter()
        Clock.schedule_once(self.addEx, .5)

    def addEx(self, dt):
        """."""
        self.ids.box.clear_widgets()
        livros = Exemplar().select(
            """
            SELECT e.id, l.titulo, e.codigo
            FROM livro l JOIN exemplar e ON l.id=e.livro_id
            ORDER BY e.livro_id
            """,
            sel='fetchall'
        )
        if len(livros) > 0:
            for i in livros:
                ex = Exibir()
                ex.texto = "Titulo: " + i.titulo + '\n' + \
                           "Codigo: " + i.codigo
                ex.height = sp(130)
                ex.idEx = i.id
                # ex.att = self.atualizar
                ex.deletar = self.deletar
                self.ids.box.add_widget(ex)
        else:
            ex = Exibir()
            ex.remove_widget(ex.ids.att)
            ex.remove_widget(ex.ids.deletar)
            ex.height = sp(50)
            ex.ids.texto.font_size = sp(20)
            ex.texto = "Não há Exemplares!"
            self.ids.box.add_widget(ex)

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
        Exemplar().delete('id', ins.idEx)
        App.get_running_app().root.current_screen.on_pre_enter()


class ExemplaresCadastrar(Tela):
    """."""

    textoBotaoCadastrar = StringProperty("Cadastrar")

    textoLabelLivro = StringProperty("Livro:")
    textoLabelCodigo = StringProperty("Código:")

    textoSpnLivro = StringProperty("Livros")

    idLivro = StringProperty('')
    codigo = StringProperty('')

    def on_pre_enter(self):
        """."""
        super().on_pre_enter()
        self.idLivro = ''
        self.codigo = ''
        self.ids.livrosSpn.text = 'Livros'
        self.ids.codigoText.text = ''
        Clock.schedule_once(self.addLivro, .5)

    def addLivro(self, dt):
        """."""
        self.ids.livrosSpn.values = []
        livros = Livro().select("SELECT id,titulo FROM livro", sel='fetchall')
        if len(livros) > 0:
            ll = []
            for i in livros:
                l = livroString(i.titulo)
                l.id = str(i.id)
                ll.append(l)
            self.ids.livrosSpn.values = ll
        else:
            self.ids.livrosSpn.text = "Não há Livros!"
            self.ids.livrosSpn.values = []

    def escolheLivro(self, args):
        """."""
        if len(args) > 1 and 'id' in dir(args[1]):
            self.idLivro = args[1].id

    def cadastrarExemplar(self):
        """."""
        p = PopupError()
        err = 0
        p.texto = ''
        if self.idLivro == '':
            p.texto += "Selecione um Livro.\n"
            err += 1
        if self.codigo == '':
            p.texto += "Digite um Codigo.\n"
            err += 1
        if err > 0:
            p.titulo = "Erro!"
            p.open()
        else:
            p.titulo = 'Sucesso!'
            p.texto = 'Cadastrado Com Sucesso!'
            p.funcao = self._mudaAoTerminar
            e = Exemplar()
            e.livro_id = self.idLivro
            e.codigo = self.codigo
            e.insert()
            p.open()

    def _mudaAoTerminar(self, instancia):
        """."""
        App.get_running_app().root.current = 'Exemplaresacervo'
        instancia.dismiss()


class livroString(str):
    """."""

    def __init__(self, dados):
        """."""
        # self.id = dados.id
        self.titulo = dados

    def __str__(self):
        """."""
        return self.titulo

    def __repr__(self):
        """."""
        return self.titulo
