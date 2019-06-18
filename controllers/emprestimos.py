"""."""
from kivy.app import App
from kivy.clock import Clock
from kivy.metrics import sp
from kivy.uix.button import Button
from kivy.properties import StringProperty, ListProperty  # pylint: disable=no-name-in-module

from models.devolucao import Devolucao  # pylint: disable=import-error
from models.emprestimo import Emprestimo  # pylint: disable=import-error

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
        e.renovacao = ins.qtdRen + 1
        e.update('id', ins.idEmp)
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
    textoSpnExemplar = StringProperty("Exemplar")
    textoSpnUsuario = StringProperty("Usuario")

    listaSpnLivro = ListProperty()
    listaSpnExemplar = ListProperty()
    listaSpnUsuario = ListProperty()
