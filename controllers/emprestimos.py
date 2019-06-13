"""."""
from .telaBase import Tela  # pylint: disable=relative-beyond-top-level
from .exibir import Exibir  # pylint: disable=relative-beyond-top-level
from models.emprestimo import Emprestimo  # pylint: disable=import-error
from models.devolucao import Devolucao  # pylint: disable=import-error
from kivy.metrics import sp


class Emprestimos(Tela):
    """."""

    def on_pre_enter(self, *args, **kwargs):
        """."""
        super().on_pre_enter()
        self.ids.box.clear_widgets()
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
        devolucoes = Devolucao().select(
            """
            SELECT l.titulo, u.nome, ee.codigo,
                   d.data_devolucao FROM devolucao d join emprestimo e on d.emprestimo_id=e.id
            join exemplar ee on e.exemplar_id = ee.id
            join livro l on ee.livro_id=l.id join usuario u on e.usuario_id=u.id
            """, sel='fetchall')
        for i in devolucoes:
            ex = Exibir()
            ex.height = sp(130)
            ex.texto = "Titulo: " + i.titulo + \
                       "\nNome Usuario: " + i.nome + \
                       "\nCodigo Exemplar: " + i.codigo + \
                       "\nData Devolução: " + i.data_devolucao.strftime("%d/%m/%Y")
            self.ids.box.add_widget(ex)


class Emprestar(Tela):
    """."""

    ...
