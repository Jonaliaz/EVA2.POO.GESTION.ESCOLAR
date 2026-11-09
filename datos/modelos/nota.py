from peewee import AutoField, FloatField, DateField, ForeignKeyField
from datos.conexion_db import BaseModel
from datos.modelos.alumno import Alumno
from datos.modelos.evaluaciones import Evaluaciones


class Nota(BaseModel):
    id_nota = AutoField()
    calificacion = FloatField()
    fecha = DateField()
    id_alumno = ForeignKeyField(Alumno, column_name='id_alumno', backref='notas')
    id_evaluaciones = ForeignKeyField(Evaluaciones, column_name='id_evaluaciones', backref='notas')

    class Meta:
        table_name = 'nota'
