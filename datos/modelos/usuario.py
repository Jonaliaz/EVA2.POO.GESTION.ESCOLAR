from peewee import AutoField, CharField, DateField, IntegerField, SQL
from datos.conexion_db import BaseModel

defecto = 'DEFAULT 1'


class Usuarios(BaseModel):
    id_usuario = AutoField()
    nombre = CharField(max_length=30)
    apellido = CharField(max_length=30, null=True)
    correo = CharField(max_length=100)
    contrasena = CharField(max_length=255)
    habilitado = IntegerField(default=1, constraints=[SQL(defecto)])
    rut = CharField(max_length=12, null=True, unique=True)

    class Meta:
        table_name = 'usuario'


Usuario = Usuarios
