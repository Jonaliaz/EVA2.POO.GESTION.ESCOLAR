from peewee import MySQLDatabase
from decouple import config

def conexio_db():
    database = MySQLDatabase(
        config('db'),
        **{
            'charset': 'utf8mb4',
            'host': config('host'),
            'port': config('port', cast=int),
            'user': config('user'),
            'password': config('password')
        }
    )
    return database