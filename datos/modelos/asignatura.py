from peewee import AutoField, CharField, ForeignKeyField
from datos.conexion_db import BaseModel
from datos.modelos.profesor import Profesor


class Asignatura(BaseModel):
    id_asignatura = AutoField()
    nombre = CharField(max_length=40)
    descripcion = CharField(max_length=100, null=True)
    id_profesor = ForeignKeyField(Profesor, column_name='id_profesor', backref='asignaturas')

    class Meta:
        table_name = 'asignatura'
