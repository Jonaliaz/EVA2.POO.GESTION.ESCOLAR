from prettytable import PrettyTable
from auxiliares.info_app import mensaje_error
from datos.modelos.nota import Nota
from datos.repositorios.repo_nota import (
    listado_notas,
    obtener_nota,
    guardar_nota,
    eliminar_nota
)


def lista_notas(tabla: PrettyTable):
    try:
        tabla.field_names = ['ID', 'Alumno', 'Evaluación', 'Calificación', 'Fecha']
        for n in listado_notas():
            tabla.add_row([n.id_nota, n.id_alumno.nombre, n.id_evaluaciones.nombre, n.calificacion, n.fecha])
        return tabla
    except Exception as error:
        print(f'{mensaje_error}{error}')


def obtener_objeto_nota(id_nota: int):
    try:
        return obtener_nota(id_nota)
    except Exception as error:
        print(f'{mensaje_error}{error}')
        return None


def crear_objeto_nota(calificacion, fecha, id_alumno, id_evaluaciones):
    try:
        nueva = Nota()
        nueva.calificacion = calificacion
        nueva.fecha = fecha
        nueva.id_alumno = id_alumno
        nueva.id_evaluaciones = id_evaluaciones
        guardar_nota(nueva)
    except Exception as error:
        print(f'{mensaje_error}{error}')


def eliminar_objeto_nota(nota: Nota):
    try:
        return eliminar_nota(nota)
    except Exception as error:
        print(f'{mensaje_error}{error}')
        return False
