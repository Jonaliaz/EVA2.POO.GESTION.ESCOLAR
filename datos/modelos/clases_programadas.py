from peewee import AutoField, CharField, DateField, ForeignKeyField
from datos.conexion_db import BaseModel
from datos.modelos.asignatura import Asignatura
from datos.modelos.seccion import Seccion


class Clases_programadas(BaseModel):
    id_clases_prog = AutoField()
    horario = CharField(max_length=35)
    fecha = DateField()
    sala = CharField(max_length=35)
    id_asignatura = ForeignKeyField(Asignatura, column_name='id_asignatura', backref='clases_programadas')
    id_seccion = ForeignKeyField(Seccion, column_name='id_seccion', backref='clases_programadas')

    class Meta:
        table_name = 'clases_programadas'
