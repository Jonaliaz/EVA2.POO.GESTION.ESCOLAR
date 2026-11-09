from peewee import MySQLDatabase, Model
from decouple import config

_database = None


def conexion_db():
    global _database
    if _database is None:
        try:
            _database = MySQLDatabase(
                config('db').strip(),
                **{
                    'charset': 'utf8mb4',
                    'host': config('host').strip(),
                    'port': int(config('port').strip()),
                    'user': config('user').strip(),
                    'password': config('password').strip()
                }
            )
        except Exception as e:
            print(f"Ha ocurrido un error en la conexion de la base de datos: {e}")
            return None
    return _database


conectar_db = conexion_db
database = conexion_db()


class BaseModel(Model):
    """Clase base que centraliza la conexion a la base de datos para todas las entidades."""
    class Meta:
        database = database
