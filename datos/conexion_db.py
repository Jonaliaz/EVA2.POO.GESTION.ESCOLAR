from peewee import MySQLDatabase
from decouple import config

def conexion_db():
    try:
        database = MySQLDatabase(
            config('db').strip(),
            **{
                'charset': 'utf8mb4',
                'host': config('host').strip(),
                'port': int(config('port').strip()),
                'user': config('user').strip(),
                'password': config('password').strip()
            }
        )
        return database
    except Exception as e:
        print(f"Ha ocurrido un error en la conexion de la base de datos: {e}")
        return None