from peewee import AutoField, CharField, IntegerField, ForeignKeyField
from datos.conexion_db import BaseModel
from datos.modelos.curso import Curso
from datos.modelos.asignatura import Asignatura


class Seccion(BaseModel):
    id_seccion = AutoField()
    numero = CharField(max_length=35)
    cupos = IntegerField()
    id_curso = ForeignKeyField(Curso, column_name='id_curso', backref='secciones')
    id_asignatura = ForeignKeyField(Asignatura, column_name='id_asignatura', backref='secciones')

    class Meta:
        table_name = 'seccion'
