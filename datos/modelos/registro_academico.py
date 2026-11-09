from peewee import AutoField, DateField, ForeignKeyField
from datos.conexion_db import BaseModel
from datos.modelos.curso import Curso
from datos.modelos.contenido import Contenido


class Registro_academico(BaseModel):
    id_registro_academico = AutoField()
    fecha = DateField()
    id_curso = ForeignKeyField(Curso, column_name='id_curso', backref='registros_academicos')
    id_contenido = ForeignKeyField(Contenido, column_name='id_contenido', backref='registros_academicos')

    class Meta:
        table_name = 'registro_academico'
