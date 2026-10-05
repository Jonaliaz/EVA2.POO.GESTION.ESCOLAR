from peeweeimport MySQLDatabase
from decoue import config



def coneccio_db :
    database = MySQLDatabase(config('db'), **{
    'charset': 'utf8mb4', 
    'host': config('host'), 
    'port': config('port'), 
    'user': config('user'), 
    'password': config('password')})
    return database