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

    @property
    def is_authenticated(self):
        """."""
        return True

    @property
    def is_active(self):
        """."""
        return True

    @property
    def is_anonymous(self):
        """."""
        return False

    def get_id(self):
        """."""
        return str(self.getDict()[self.__pk__])

    def procurarUsuarioPeloEmail(self, email: str):
        """."""
        usuario = self.select(
            'select * from usuario where email = %(email)s',
            {'email': email}
            )
        return usuario if usuario else None

    def criptografar_senha(self, password):
        """."""
        self.__dict__[password] = pbkdf2_sha256.hash(self.__dict__[password])

    def verify_password(self, campoPassword, password):
        """."""
        return pbkdf2_sha256.verify(password, self.__dict__[campoPassword])
