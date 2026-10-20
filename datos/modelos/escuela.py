from peewee import (
    Model,
    AutoField,
    CharField,
    IntegerField,
    FloatField,
    DateField,
    ForeignKeyField
)
from datos.conexion_db import conexion_db

database = conexion_db()

class BaseModel(Model):
    """Clase base que centraliza la conexion a la base de datos para todas las entidades."""
    class Meta:
        database = database
        
        
class Apoderado(BaseModel):
    id_apoderado = AutoField()
    nombre = CharField(max_length=40)
    correo = CharField(max_length=50)
    telefono = CharField(max_length=50)
    
    class Meta:
        table_name = 'apoderado'
        
        
class Curso(BaseModel):
    id_curso = AutoField()
    nombre = CharField(max_length=30)
    nivel = CharField(max_length=20)
    
    class Meta:
        table_name ='curso'
        
        
class Profesor(BaseModel):
    id_profesor = AutoField()
    nombre = CharField(max_length=50)
    correo = CharField(max_length=60)
    telefono = CharField(max_length=18)
    
    class Meta:
        table_name = 'profesor'
        
        
class Asignatura(BaseModel):
    id_asignatura = AutoField()
    nombre = CharField(max_length=40)
    descripcion = CharField(max_length=100, null=True)
    id_profesor = ForeignKeyField(Profesor, column_name='id_profesor', backref='asignaturas')
    
    class Meta:
        table_name = 'asignatura'
        
        
class Contenido(BaseModel):
    id_contenido = AutoField()
    nombre = CharField(max_length=40)
    numero_unidad = IntegerField()
    
    class Meta:
        table_name = 'contenido'
        
        
class Evaluaciones(BaseModel):
    id_evaluaciones = AutoField()
    nombre = CharField(max_length=30)
    fecha = DateField()
    descripcion = CharField(max_length=40)
    id_contenido = ForeignKeyField(Contenido, column_name='id_contenido', backref='evaluaciones')
    
    class Meta:
        table_name = 'evaluaciones'
        
        
class Seccion(BaseModel):
    id_seccion = AutoField()
    numero = CharField(max_length=35)
    cupos = IntegerField()
    id_curso = ForeignKeyField(Curso, column_name='id_curso', backref='secciones')
    id_asignatura = ForeignKeyField(Asignatura, column_name='id_asignatura', backref='secciones')
    
    class Meta:
        table_name = 'seccion'
        
        
class Alumno(BaseModel):
    id_alumno = AutoField()
    nombre = CharField(max_length=60)
    correo = CharField(max_length=50)
    telefono = CharField(max_length=50)
    id_seccion = ForeignKeyField(Seccion, column_name='id_seccion', backref='alumnos')
    id_curso = ForeignKeyField(Curso, column_name='id_curso', backref='alumnos')
    id_apoderado = ForeignKeyField(Apoderado, column_name='id_apoderado', backref='alumnos')
    
    class Meta:
        table_name = 'Alumno'
        
        
class Registro_academico(BaseModel):
    id_registro_academico = AutoField()
    fecha = DateField()
    id_curso = ForeignKeyField(Curso, column_name='id_curso', backref='registros_academicos')
    id_contenido = ForeignKeyField(Contenido, column_name='id_contenido', backref='registros_academicos')
    
    class Meta:
        table_name = 'registro_academico'
        
        
class Clases_programadas(BaseModel):
    id_clases_prog = AutoField()
    horario = CharField(max_length=35)
    fecha = DateField()
    sala = CharField(max_length=35)
    id_asignatura = ForeignKeyField(Asignatura, column_name='id_asignatura', backref='clases_programadas')
    id_seccion = ForeignKeyField(Seccion, column_name='id_seccion', backref='clases_programadas')
    
    class Meta:
        table_name = 'clases_programadas'
        
        
class Nota(BaseModel):
    id_nota = AutoField()
    calificacion = FloatField()
    fecha = DateField()
    id_alumno = ForeignKeyField(Alumno, column_name='id_alumno', backref='notas')
    id_evaluaciones = ForeignKeyField(Evaluaciones, column_name='id_evaluaciones', backref='notas')
    
    class Meta:
        table_name = 'nota'
        
        
class Asistencia(BaseModel):
    id_asistencia = AutoField()
    fecha = DateField()
    estado = CharField(max_length=30)
    id_alumno = ForeignKeyField(Alumno, column_name='id_alumno', backref='asistencias')
    id_clases_prog = ForeignKeyField(Clases_programadas, column_name='id_clases_prog', backref='asistencias')
    
    class Meta:
        table_name = 'asistencia'
        