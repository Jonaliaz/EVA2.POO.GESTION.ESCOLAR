from prettytable import PrettyTable
from auxiliares.info_app import mensaje_error
from datos.modelos.evaluaciones import Evaluaciones
from datos.repositorios.repo_evaluaciones import (
    listado_evaluaciones,
    obtener_evaluacion,
    guardar_evaluacion,
    eliminar_evaluacion
)


def lista_evaluaciones(tabla: PrettyTable):
    try:
        tabla.field_names = ['ID', 'Evaluación', 'Fecha', 'Descripción', 'Contenido']
        for ev in listado_evaluaciones():
            tabla.add_row([ev.id_evaluaciones, ev.nombre, ev.fecha, ev.descripcion, ev.id_contenido.nombre])
        return tabla
    except Exception as error:
        print(f'{mensaje_error}{error}')


def obtener_objeto_evaluacion(id_evaluaciones: int):
    try:
        return obtener_evaluacion(id_evaluaciones)
    except Exception as error:
        print(f'{mensaje_error}{error}')
        return None


def crear_objeto_evaluacion(nombre, fecha, descripcion, id_contenido):
    try:
        nueva = Evaluaciones()
        nueva.nombre = nombre
        nueva.fecha = fecha
        nueva.descripcion = descripcion
        nueva.id_contenido = id_contenido
        guardar_evaluacion(nueva)
    except Exception as error:
        print(f'{mensaje_error}{error}')


def eliminar_objeto_evaluacion(evaluacion: Evaluaciones):
    try:
        return eliminar_evaluacion(evaluacion)
    except Exception as error:
        print(f'{mensaje_error}{error}')
        return False
