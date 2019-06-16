"""."""
from . import Model
from passlib.hash import pbkdf2_sha256


class Usuario(Model):
    """Model da Tabela ."""

    def __init__(self, lista: dict = {}):
        """."""
        super().__init__(lista)
        self.__table__ = 'usuario'
        self.__pk__ = 'id'

    def procurarUsuarioPeloEmail(self, email: str):
        """."""
        usuario = self.select(
            'select * from usuario where email = %(email)s',
            {'email': email}
            )
        return usuario if usuario else None

    def criptografar_senha(self, password):
        """Criptografa a Senha."""
        self.__dict__[password] = pbkdf2_sha256.hash(self.__dict__[password])

    def verify_password(self, campoPassword, password):
        """Verifica se a Senha está Correta."""
        return pbkdf2_sha256.verify(password, self.__dict__[campoPassword])
