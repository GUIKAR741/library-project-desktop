"""Model Base do Banco."""
import pymysql

from .config import (MYSQL_DATABASE_CHARSET, MYSQL_DATABASE_DB,
                     MYSQL_DATABASE_HOST, MYSQL_DATABASE_PASSWORD,
                     MYSQL_DATABASE_PORT, MYSQL_DATABASE_USER)


class sql:
    """Classe para Executar Comandos SQL."""

    def __init__(self):
        """
        Metodo Inicializador da Classe SQL.

        Abre a Conexão
        """
        self.conn = pymysql.connect(host=MYSQL_DATABASE_HOST,
                                    user=MYSQL_DATABASE_USER,
                                    password=MYSQL_DATABASE_PASSWORD,
                                    db=MYSQL_DATABASE_DB,
                                    port=MYSQL_DATABASE_PORT,
                                    charset=MYSQL_DATABASE_CHARSET,
                                    cursorclass=pymysql.cursors.DictCursor)
        self.rows = None

    def __del__(self):
        """
        Metodo Destrutor da Classe SQL.

        Fecha a Conexão
        """
        self.conn.close()

    def _query(self, sql: str, campos: str = None):
        """Executa as Querys."""
        cursor = self.conn.cursor()
        self.rows = cursor.execute(sql, campos)
        return cursor

    def select(self, sql, campos=None, sel='fetchone'):
        """Executa Select no Banco de Dados."""
        curr = self._query(sql, campos)
        if sel == 'fetchone':
            sel = curr.fetchone()
        if sel == 'fetchall':
            sel = curr.fetchall()
        return sel

    def operacao(self, sql, campos=None):
        """Executa Select no Banco de Dados."""
        self._query(sql, campos)
        self.conn.commit()
        return self.rows


class Model(object):
    """Classe de Model para Interface com o Banco."""

    def __init__(self, lista: dict = {}):
        """Metodo Inicializador da Classe."""
        self.__dict__ = dict(lista) if type(lista) == dict else {}
        self.__table__ = None
        self.__pk__ = None

    def __repr__(self):
        """Representação do Objeto."""
        return str(self.getDict())

    def getDict(self):
        """Retorna Um dicionario com os dados do model."""
        return {i: j for i, j in filter(lambda x: not (
            x[0] in ['__table__', '__pk__']), self.__dict__.items())}

    def setPK(self, campo):
        """Metodo para escolhar a chave primaria da tabela."""
        if campo in self.__dict__.keys():
            self.__pk__ = campo
        else:
            raise AttributeError('Campo Não Definido na Tabela')

    def insert(self):
        """Insere os dados na tabela com os campos adicionados."""
        campos = ", ".join(self.getDict().keys())
        values = ", ".join(map(lambda x: f"%({x})s", self.getDict().keys()))
        return sql().operacao(
            f"INSERT INTO {self.__table__}({campos}) VALUES ({values})",
            self.getDict()
        )

    def update(self, campo, val):
        """Atualiza os campos da tabela."""
        dic = self.getDict()
        campos = ', '.join(
            map(lambda x: ' = '.join(x),
                zip(
                    filter(
                        lambda x: not (self.__pk__ == x),
                        dic.keys()
                    ),
                    map(lambda x: f"%({x})s",
                        filter(
                            lambda x: not (self.__pk__ == x),
                            dic.keys()
                        )
                        )
                    )
                )
            )
        dic[campo] = val
        return sql().operacao(
            f"UPDATE {self.__table__} "
            f"SET {campos} where {campo} = %({campo})s",
            dic
        )

    def delete(self, campo, val):
        """Remove o registro da Tabela."""
        return sql().operacao(
            f"DELETE FROM {self.__table__} WHERE {campo} = %({campo})s",
            {campo: val}
        )

    def select(self, sqlstr: str, campos=None, sel='fetchone'):
        """Seleciona Registros da Tabela."""
        if sel == 'fetchone':
            model = None
            items = sql().select(sqlstr, campos, sel)
            if items:
                model = self.__class__(items)
        elif sel == 'fetchall':
            model = sql().select(sqlstr, campos, sel)
            model = [self.__class__(i) for i in model]
        return model
