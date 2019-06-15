"""."""
from kivy.metrics import sp
from kivy.clock import Clock
from kivy.uix.button import Button

from models.devolucao import Devolucao  # pylint: disable=import-error
from models.emprestimo import Emprestimo  # pylint: disable=import-error

from .exibir import Exibir  # pylint: disable=relative-beyond-top-level
from .telaBase import Tela  # pylint: disable=relative-beyond-top-level


class Emprestimos(Tela):
    """."""

    def on_pre_enter(self, *args, **kwargs):
        """."""
        super().on_pre_enter()
        self.ids.box.clear_widgets()
        Clock.schedule_once(self.addEmp, 0.5)

    def addEmp(self, dt):
        """."""
        livros = Emprestimo().select(
            """
            SELECT l.titulo, u.nome, ee.codigo, e.renovacao,
                   e.data_devolucao_estimada FROM emprestimo e
            join exemplar ee on e.exemplar_id = ee.id
            join livro l on ee.livro_id=l.id join usuario u on e.usuario_id=u.id
            where status=0
            """, sel='fetchall')
        for i in livros:
            ex = Exibir()
            novoTexto = ["Devolver", "Renovar"]
            text = list(filter(lambda x: type(x) is Button, ex.children))
            for j in range(len(text)):
                text[j].text = novoTexto[j]
            ex.height = sp(130)
            ex.texto = "Titulo: " + i.titulo + \
                       "\nNome Usuario: " + i.nome + \
                       "\nCodigo Exemplar: " + i.codigo + \
                       "\nRenocações:  " + str(i.renovacao) + \
                       "\nData Prevista Devolução: " + \
                       i.data_devolucao_estimada.strftime("%d/%m/%Y")
            self.ids.box.add_widget(ex)


class Devolucoes(Tela):
    """."""

    def on_pre_enter(self, *args, **kwargs):
        """."""
        super().on_pre_enter()
        self.ids.box.clear_widgets()
        Clock.schedule_once(self.addDev, 0.5)

    def addDev(self, dt):
        """."""
        devolucoes = Devolucao().select(
            """
            SELECT l.titulo, u.nome, ee.codigo,
                   d.data_devolucao FROM devolucao d join emprestimo e on d.emprestimo_id=e.id
            join exemplar ee on e.exemplar_id = ee.id
            join livro l on ee.livro_id=l.id join usuario u on e.usuario_id=u.id
            """, sel='fetchall')
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
                i.data_devolucao.strftime("%d/%m/%Y")
            self.ids.box.add_widget(ex)


class Emprestar(Tela):
    """."""

    ...
