from peewee import AutoField, CharField
from datos.conexion_db import BaseModel


class Apoderado(BaseModel):
    id_apoderado = AutoField()
    nombre = CharField(max_length=40)
    correo = CharField(max_length=50)
    telefono = CharField(max_length=50)

    class Meta:
        table_name = 'apoderado'
