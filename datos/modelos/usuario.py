from peewee import AutoField, CharField, DateField, IntegerField, SQL
from datos.conexion_db import BaseModel

defecto = 'DEFAULT 1'


class Usuarios(BaseModel):
    id_usuario = AutoField()
    nombre = CharField(max_length=25)
    apellido = CharField(max_length=25, null=True)
    correo = CharField()
    fecha_incorporacion = DateField(null=True)
    fecha_nacimiento = DateField(null=True)
    genero = IntegerField(null=True)
    habilitado = IntegerField(default=1, constraints=[SQL(defecto)])
    pais = IntegerField(index=True, null=True)
    rut = CharField(max_length=11, null=True, unique=True)

    class Meta:
        table_name = 'usuarios'


Usuario = Usuarios
