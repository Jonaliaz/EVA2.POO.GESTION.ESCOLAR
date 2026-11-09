from prettytable import PrettyTable
from auxiliares.info_app import mensaje_error
from datos.modelos.curso import Curso
from datos.repositorios.repo_curso import (
    listado_cursos,
    obtener_curso,
    guardar_curso,
    eliminar_curso
)


def lista_cursos(tabla: PrettyTable):
    try:
        tabla.field_names = ['ID', 'Nombre Curso', 'Nivel']
        for c in listado_cursos():
            tabla.add_row([c.id_curso, c.nombre, c.nivel])
        return tabla
    except Exception as error:
        print(f'{mensaje_error}{error}')


def obtener_objeto_curso(id_curso: int):
    try:
        return obtener_curso(id_curso)
    except Exception as error:
        print(f'{mensaje_error}{error}')
        return None


def crear_objeto_curso(nombre, nivel):
    try:
        nuevo = Curso()
        nuevo.nombre = nombre
        nuevo.nivel = nivel
        guardar_curso(nuevo)
    except Exception as error:
        print(f'{mensaje_error}{error}')


def actualizar_objeto_curso(nombre, nivel, curso: Curso):
    try:
        if nombre != '':
            curso.nombre = nombre
        if nivel != '':
            curso.nivel = nivel
        guardar_curso(curso)
    except Exception as error:
        print(f'{mensaje_error}{error}')


def eliminar_objeto_curso(curso: Curso):
    try:
        return eliminar_curso(curso)
    except Exception as error:
        print(f'{mensaje_error}{error}')
        return False
