from prettytable import PrettyTable
from auxiliares.info_app import mensaje_error
from datos.modelos.asistencia import Asistencia
from datos.repositorios.repo_asistencia import (
    listado_asistencias,
    obtener_asistencia,
    guardar_asistencia,
    eliminar_asistencia
)


def lista_asistencias(tabla: PrettyTable):
    try:
        tabla.field_names = ['ID', 'Fecha', 'Estado', 'Alumno', 'Horario Clase', 'Sala']
        for asis in listado_asistencias():
            tabla.add_row([
                asis.id_asistencia,
                asis.fecha,
                asis.estado,
                asis.id_alumno.nombre,
                asis.id_clases_prog.horario,
                asis.id_clases_prog.sala
            ])
        return tabla
    except Exception as error:
        print(f'{mensaje_error}{error}')


def obtener_objeto_asistencia(id_asistencia: int):
    try:
        return obtener_asistencia(id_asistencia)
    except Exception as error:
        print(f'{mensaje_error}{error}')
        return None


def crear_objeto_asistencia(fecha, estado, id_alumno, id_clases_prog):
    try:
        nueva = Asistencia()
        nueva.fecha = fecha
        nueva.estado = estado
        nueva.id_alumno = id_alumno
        nueva.id_clases_prog = id_clases_prog
        guardar_asistencia(nueva)
    except Exception as error:
        print(f'{mensaje_error}{error}')


def eliminar_objeto_asistencia(asistencia: Asistencia):
    try:
        return eliminar_asistencia(asistencia)
    except Exception as error:
        print(f'{mensaje_error}{error}')
        return False
