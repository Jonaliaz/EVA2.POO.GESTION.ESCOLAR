from peewee import AutoField, CharField
from datos.conexion_db import BaseModel


class Profesor(BaseModel):
    id_profesor = AutoField()
    nombre = CharField(max_length=50)
    correo = CharField(max_length=60)
    telefono = CharField(max_length=18)

    class Meta:
        table_name = 'profesor'
