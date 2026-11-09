from prettytable import PrettyTable
from auxiliares.info_app import mensaje_error
from datos.modelos.alumno import Alumno
from datos.modelos.curso import Curso
from datos.repositorios.repo_alumno import (
    listado_alumnos,
    obtener_alumno,
    guardar_alumno,
    eliminar_alumno,
    asignar_curso
)


def lista_alumnos(tabla: PrettyTable):
    try:
        tabla.field_names = ['ID', 'Nombre', 'Correo', 'Teléfono', 'Curso', 'Sección', 'Apoderado']
        for a in listado_alumnos():
            tabla.add_row([
                a.id_alumno,
                a.nombre,
                a.correo,
                a.telefono,
                a.id_curso.nombre,
                a.id_seccion.numero,
                a.id_apoderado.nombre
            ])
        return tabla
    except Exception as error:
        print(f'{mensaje_error}{error}')


def obtener_objeto_alumno(id_alumno: int):
    try:
        return obtener_alumno(id_alumno)
    except Exception as error:
        print(f'{mensaje_error}{error}')
        return None


def crear_objeto_alumno(nombre, correo, telefono, id_seccion, id_curso, id_apoderado):
    try:
        nuevo = Alumno()
        nuevo.nombre = nombre
        nuevo.correo = correo
        nuevo.telefono = telefono
        nuevo.id_seccion = id_seccion
        nuevo.id_curso = id_curso
        nuevo.id_apoderado = id_apoderado
        guardar_alumno(nuevo)
    except Exception as error:
        print(f'{mensaje_error}{error}')


def actualizar_objeto_alumno(nombre, correo, telefono, id_seccion, id_curso, id_apoderado, alumno: Alumno):
    try:
        if nombre != '':
            alumno.nombre = nombre
        if correo != '':
            alumno.correo = correo
        if telefono != '':
            alumno.telefono = telefono
        if id_seccion != '':
            alumno.id_seccion = int(id_seccion)
        if id_curso != '':
            alumno.id_curso = int(id_curso)
        if id_apoderado != '':
            alumno.id_apoderado = int(id_apoderado)
        guardar_alumno(alumno)
    except Exception as error:
        print(f'{mensaje_error}{error}')


def eliminar_objeto_alumno(alumno: Alumno):
    try:
        return eliminar_alumno(alumno)
    except Exception as error:
        print(f'{mensaje_error}{error}')
        return False


def asignar_curso_alumno(alumno: Alumno, curso: Curso):
    try:
        return asignar_curso(alumno, curso)
    except Exception as error:
        print(f'{mensaje_error}{error}')
        return False
