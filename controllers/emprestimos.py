"""."""
from kivy.app import App
from kivy.clock import Clock
from kivy.metrics import sp
from kivy.uix.button import Button
from kivy.properties import StringProperty, ListProperty  # pylint: disable=no-name-in-module

from models.devolucao import Devolucao  # pylint: disable=import-error
from models.emprestimo import Emprestimo  # pylint: disable=import-error
from models.exemplar import Exemplar  # pylint: disable=import-error
from models.reserva import Reserva  # pylint: disable=import-error

from .exibir import Exibir  # pylint: disable=relative-beyond-top-level
from .popuperror import PopupError  # pylint: disable=relative-beyond-top-level
from .telaBase import Tela  # pylint: disable=relative-beyond-top-level


class Emprestimos(Tela):
    """."""

    def on_pre_enter(self, *args, **kwargs):
        """."""
        super().on_pre_enter()
        Clock.schedule_once(self.addEmp, 0.5)

    def addEmp(self, dt):
        """."""
        self.ids.box.clear_widgets()
        livros = Emprestimo().select(
            """
            SELECT e.id, l.titulo, u.nome, ee.codigo, e.renovacao,
                   e.data_devolucao_estimada FROM emprestimo e
            join exemplar ee on e.exemplar_id = ee.id
            join livro l on ee.livro_id=l.id join usuario u on e.usuario_id=u.id
            where status=0
            order by id desc
            """, sel='fetchall')
        if len(livros) > 0:
            for i in livros:
                ex = Exibir()
                ex.idEmp = i.id
                ex.qtdRen = i.renovacao
                ex.ids.att.text = 'Renovar'
                ex.att = self.renovar
                ex.deletar = self.devolver
                ex.ids.deletar.text = 'Devolver'
                ex.height = sp(130)
                ex.texto = "Titulo: " + i.titulo + \
                           "\nNome Usuario: " + i.nome + \
                           "\nCodigo Exemplar: " + i.codigo + \
                           "\nRenocações:  " + str(i.renovacao) + \
                           "\nData Prevista Devolução: " + \
                           i.data_devolucao_estimada.strftime("%d/%m/%Y")
                self.ids.box.add_widget(ex)
        else:
            ex = Exibir()
            ex.remove_widget(ex.ids.att)
            ex.remove_widget(ex.ids.deletar)
            ex.height = sp(50)
            ex.ids.texto.font_size = sp(20)
            ex.texto = "Não há Emprestimos!"
            self.ids.box.add_widget(ex)

    def renovar(self, ins):
        """."""
        p = PopupError()
        p.titulo = "Deseja Realmente Renovar?"
        p.size_hint_y = .2
        p.ids.box.clear_widgets()
        sim = Button(text='sim')
        sim.size_hint_y = None
        sim.height = sp(40)
        sim.on_release = (lambda: self.ren_sim(ins, p))
        nao = Button(text='não')
        nao.size_hint_y = None
        nao.height = sp(40)
        nao.on_release = p.dismiss
        p.ids.box.orientation = 'horizontal'
        p.ids.box.add_widget(sim)
        p.ids.box.add_widget(nao)
        p.open()

    def ren_sim(self, ins, p):
        """."""
        p.dismiss()
        e = Emprestimo()
        e._op(
            '''
            UPDATE emprestimo SET renovacao = renovacao+1,
            data_devolucao_estimada = DATE_ADD(data_devolucao_estimada, INTERVAL 1 MONTH)
            WHERE id = %(idE)s
            ''',
            {'idE': ins.idEmp}
        )
        App.get_running_app().root.current_screen.on_pre_enter()

    def devolver(self, ins):
        """."""
        p = PopupError()
        p.titulo = "Deseja Realmente Devolver?"
        p.size_hint_y = .2
        p.ids.box.clear_widgets()
        sim = Button(text='sim')
        sim.size_hint_y = None
        sim.height = sp(40)
        sim.on_release = (lambda: self.dev_sim(ins, p))
        nao = Button(text='não')
        nao.size_hint_y = None
        nao.height = sp(40)
        nao.on_release = p.dismiss
        p.ids.box.orientation = 'horizontal'
        p.ids.box.add_widget(sim)
        p.ids.box.add_widget(nao)
        p.open()

    def dev_sim(self, ins, p):
        """."""
        p.dismiss()
        e = Emprestimo()
        e.status = 1
        e.update('id', ins.idEmp)
        ee = Exemplar()
        ee.disponivel = 1
        cod = e.select(
            "SELECT exemplar_id FROM emprestimo WHERE id=%(idE)s",
            {'idE': ins.idEmp}
        ).exemplar_id
        ee.update("id", cod)
        App.get_running_app().root.current_screen.on_pre_enter()


class Devolucoes(Tela):
    """."""

    def on_pre_enter(self, *args, **kwargs):
        """."""
        super().on_pre_enter()
        Clock.schedule_once(self.addDev, 0.5)

    def addDev(self, dt):
        """."""
        self.ids.box.clear_widgets()
        devolucoes = Devolucao().select(
            """
            SELECT l.titulo, u.nome, ee.codigo,
                   d.data_devolucao, d.multa FROM devolucao d
            join emprestimo e on d.emprestimo_id=e.id
            join exemplar ee on e.exemplar_id = ee.id
            join livro l on ee.livro_id=l.id join usuario u on e.usuario_id=u.id
            order by d.data_devolucao desc
            """, sel='fetchall')
        if len(devolucoes) > 0:
            for i in devolucoes:
                ex = Exibir()
                text = list(filter(lambda x: type(x) is Button, ex.children))
                for j in range(len(text)):
                    ex.remove_widget(text[j])
                ex.height = sp(130)
                ex.texto = "Titulo: " + i.titulo + \
                           "\nNome Usuario: " + i.nome + \
                           "\nCodigo Exemplar: " + i.codigo + \
                           "\nData Devolução: " + \
                           i.data_devolucao.strftime("%d/%m/%Y") + \
                           "\nMulta: " + \
                           str(i.multa)
                self.ids.box.add_widget(ex)
        else:
            ex = Exibir()
            ex.remove_widget(ex.ids.att)
            ex.remove_widget(ex.ids.deletar)
            ex.height = sp(50)
            ex.ids.texto.font_size = sp(20)
            ex.texto = "Não há Devoluções!"
            self.ids.box.add_widget(ex)


class Emprestar(Tela):
    """."""

    textoBotaoEmprestar = StringProperty("Emprestar")

    textoLabelLivro = StringProperty("Livro:")
    textoLabelExemplar = StringProperty("Exemplar:")
    textoLabelUsuario = StringProperty("Usuario:")

    textoSpnLivro = StringProperty("Livro")
    textoSpnExemplar = StringProperty("Selecione Um Livro")
    textoSpnUsuario = StringProperty("Usuario")

    listaSpnLivro = ListProperty()
    listaSpnExemplar = ListProperty()
    listaSpnUsuario = ListProperty()

    idExemplar = StringProperty('')
    idLivro = StringProperty('')
    idUsuario = StringProperty('')

    def on_pre_enter(self):
        """."""
        super().on_pre_enter()
        self.listaSpnExemplar = []
        self.idExemplar = ''
        self.idLivro = ''
        self.idUsuario = ''
        self.ids.livrosSpn.text = "Livro"
        self.ids.exemplarSpn.text = "Selecione Um Livro"
        self.ids.usuariosSpn.text = "Usuario"
        Clock.schedule_once(self.addLivro, .5)
        Clock.schedule_once(self.addUsuario, .5)

    def addLivro(self, dt):
        """."""
        self.listaSpnLivro = []
        self.textoSpnLivro = "Livro"
        livros = Emprestimo().select("SELECT id,titulo FROM livro", sel='fetchall')
        if len(livros) > 0:
            ll = []
            for i in livros:
                l = NovaString(i.titulo)
                l.id = str(i.id)
                ll.append(l)
            self.listaSpnLivro = ll
        else:
            self.textoSpnLivro = "Não há Livros!"
            self.listaSpnLivro = []

    def escolheExemplar(self, args):
        """."""
        if len(args) > 1 and 'id' in dir(args[1]):
            self.idExemplar = args[1].id

    def addExemplar(self, args):
        """."""
        if len(args) > 1 and 'id' in dir(args[1]):
            lid = args[1].id
            self.idLivro = str(lid)
            self.listaSpnExemplar = []
            self.ids.exemplarSpn.text = "Exemplares"
            livros = Emprestimo().select(
                """SELECT id,codigo FROM exemplar WHERE livro_id=%(lid)s
                and disponivel=1""",
                {'lid': lid},
                sel='fetchall')
            if len(livros) > 0:
                ll = []
                for i in livros:
                    l = NovaString(i.codigo)
                    l.id = str(i.id)
                    ll.append(l)
                self.listaSpnExemplar = ll
            else:
                self.ids.exemplarSpn.text = "Não há Exemplares!"
                self.listaSpnExemplar = []

    def addUsuario(self, dt):
        """."""
        self.listaSpnUsuario = []
        self.textoSpnUsuario = "Usuario"
        livros = Emprestimo().select("SELECT id,nome FROM usuario WHERE tipo=0", sel='fetchall')
        if len(livros) > 0:
            ll = []
            for i in livros:
                l = NovaString(i.nome)
                l.id = str(i.id)
                ll.append(l)
            self.listaSpnUsuario = ll
        else:
            self.textoSpnUsuario = "Não há Usuarios!"
            self.listaSpnUsuario = []

    def emprestar(self):
        """."""
        p = PopupError()
        err = 0
        p.texto = ''
        if self.idExemplar == '':
            p.texto += "Selecione um Livro e Um Exemplar.\n"
            err += 1
        if self.idUsuario == '':
            p.texto += "Selecione Um Usuario.\n"
            err += 1
        if err > 0:
            p.titulo = "Erro!"
            p.open()
        else:
            p.titulo = 'Sucesso!'
            p.texto = 'Cadastrado Com Sucesso!'
            p.funcao = self._mudaAoTerminar
            e = Exemplar()
            e.disponivel = 0
            e.update('id', self.idExemplar)
            e._op(
                """
                INSERT INTO emprestimo(usuario_id, exemplar_id, data_devolucao_estimada)
                VALUES (%(idU)s, %(idE)s, DATE_ADD(CURRENT_TIMESTAMP, INTERVAL 1 MONTH))""",
                {'idU': self.idUsuario, 'idE': self.idExemplar}
                )
            reserva = e.select(
                """
                SELECT id FROM reserva
                WHERE livro_id=%(idL)s and usuario_id=%(idU)s
                """,
                {'idU': self.idUsuario, 'idL': self.idLivro}
                )
            if reserva:
                r = Reserva()
                r.status = 0
                r.update('id', reserva.id)
            p.open()

    def _mudaAoTerminar(self, instancia):
        """."""
        App.get_running_app().root.current = 'VerTodosemprestimos'
        instancia.dismiss()


class NovaString(str):
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
