from peewee import AutoField, CharField, DateField, ForeignKeyField
from datos.conexion_db import BaseModel
from datos.modelos.alumno import Alumno
from datos.modelos.clases_programadas import Clases_programadas


class Asistencia(BaseModel):
    id_asistencia = AutoField()
    fecha = DateField()
    estado = CharField(max_length=30)
    id_alumno = ForeignKeyField(Alumno, column_name='id_alumno', backref='asistencias')
    id_clases_prog = ForeignKeyField(Clases_programadas, column_name='id_clases_prog', backref='asistencias')

    class Meta:
        table_name = 'asistencia'
