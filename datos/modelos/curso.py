from peewee import AutoField, CharField
from datos.conexion_db import BaseModel


class Curso(BaseModel):
    id_curso = AutoField()
    nombre = CharField(max_length=30)
    nivel = CharField(max_length=20)

    class Meta:
        table_name = 'curso'
