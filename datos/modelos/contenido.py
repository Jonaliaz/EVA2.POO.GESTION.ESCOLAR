from peewee import AutoField, CharField, IntegerField
from datos.conexion_db import BaseModel


class Contenido(BaseModel):
    id_contenido = AutoField()
    nombre = CharField(max_length=40)
    numero_unidad = IntegerField()

    class Meta:
        table_name = 'contenido'
