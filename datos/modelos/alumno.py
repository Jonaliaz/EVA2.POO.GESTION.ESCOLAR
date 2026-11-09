from peewee import AutoField, CharField, ForeignKeyField
from datos.conexion_db import BaseModel
from datos.modelos.seccion import Seccion
from datos.modelos.curso import Curso
from datos.modelos.apoderado import Apoderado


class Alumno(BaseModel):
    id_alumno = AutoField()
    nombre = CharField(max_length=60)
    correo = CharField(max_length=50)
    telefono = CharField(max_length=50)
    id_seccion = ForeignKeyField(Seccion, column_name='id_seccion', backref='alumnos')
    id_curso = ForeignKeyField(Curso, column_name='id_curso', backref='alumnos')
    id_apoderado = ForeignKeyField(Apoderado, column_name='id_apoderado', backref='alumnos')

    class Meta:
        table_name = 'alumno'
