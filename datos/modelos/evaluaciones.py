from peewee import AutoField, CharField, DateField, ForeignKeyField
from datos.conexion_db import BaseModel
from datos.modelos.contenido import Contenido


class Evaluaciones(BaseModel):
    id_evaluaciones = AutoField()
    nombre = CharField(max_length=30)
    fecha = DateField()
    descripcion = CharField(max_length=40)
    id_contenido = ForeignKeyField(Contenido, column_name='id_contenido', backref='evaluaciones')

    class Meta:
        table_name = 'evaluaciones'
