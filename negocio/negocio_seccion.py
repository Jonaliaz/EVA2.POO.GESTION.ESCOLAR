from prettytable import PrettyTable
from auxiliares.info_app import mensaje_error
from datos.modelos.seccion import Seccion
from datos.repositorios.repo_seccion import (
    listado_secciones,
    obtener_seccion,
    guardar_seccion,
    eliminar_seccion
)


def lista_secciones(tabla: PrettyTable):
    try:
        tabla.field_names = ['ID', 'Número Sección', 'Cupos', 'Curso', 'Asignatura']
        for s in listado_secciones():
            tabla.add_row([s.id_seccion, s.numero, s.cupos, s.id_curso.nombre, s.id_asignatura.nombre])
        return tabla
    except Exception as error:
        print(f'{mensaje_error}{error}')


def obtener_objeto_seccion(id_seccion: int):
    try:
        return obtener_seccion(id_seccion)
    except Exception as error:
        print(f'{mensaje_error}{error}')
        return None


def crear_objeto_seccion(numero, cupos, id_curso, id_asignatura):
    try:
        nueva = Seccion()
        nueva.numero = numero
        nueva.cupos = cupos
        nueva.id_curso = id_curso
        nueva.id_asignatura = id_asignatura
        guardar_seccion(nueva)
    except Exception as error:
        print(f'{mensaje_error}{error}')


def actualizar_objeto_seccion(numero, cupos, id_curso, id_asignatura, seccion: Seccion):
    try:
        if numero != '':
            seccion.numero = numero
        if cupos != '':
            seccion.cupos = int(cupos)
        if id_curso != '':
            seccion.id_curso = int(id_curso)
        if id_asignatura != '':
            seccion.id_asignatura = int(id_asignatura)
        guardar_seccion(seccion)
    except Exception as error:
        print(f'{mensaje_error}{error}')


def eliminar_objeto_seccion(seccion: Seccion):
    try:
        return eliminar_seccion(seccion)
    except Exception as error:
        print(f'{mensaje_error}{error}')
        return False
