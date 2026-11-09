from prettytable import PrettyTable
from auxiliares.info_app import mensaje_error
from datos.modelos.asignatura import Asignatura
from datos.repositorios.repo_asignatura import (
    listado_asignaturas,
    obtener_asignatura,
    guardar_asignatura,
    eliminar_asignatura
)


def lista_asignaturas(tabla: PrettyTable):
    try:
        tabla.field_names = ['ID', 'Asignatura', 'Descripción', 'Profesor']
        for asig in listado_asignaturas():
            tabla.add_row([asig.id_asignatura, asig.nombre, asig.descripcion, asig.id_profesor.nombre])
        return tabla
    except Exception as error:
        print(f'{mensaje_error}{error}')


def obtener_objeto_asignatura(id_asignatura: int):
    try:
        return obtener_asignatura(id_asignatura)
    except Exception as error:
        print(f'{mensaje_error}{error}')
        return None


def crear_objeto_asignatura(nombre, descripcion, id_profesor):
    try:
        nueva = Asignatura()
        nueva.nombre = nombre
        nueva.descripcion = descripcion
        nueva.id_profesor = id_profesor
        guardar_asignatura(nueva)
    except Exception as error:
        print(f'{mensaje_error}{error}')


def actualizar_objeto_asignatura(nombre, descripcion, id_profesor, asignatura: Asignatura):
    try:
        if nombre != '':
            asignatura.nombre = nombre
        if descripcion != '':
            asignatura.descripcion = descripcion
        if id_profesor != '':
            asignatura.id_profesor = int(id_profesor)
        guardar_asignatura(asignatura)
    except Exception as error:
        print(f'{mensaje_error}{error}')


def eliminar_objeto_asignatura(asignatura: Asignatura):
    try:
        return eliminar_asignatura(asignatura)
    except Exception as error:
        print(f'{mensaje_error}{error}')
        return False
