from prettytable import PrettyTable
from auxiliares.info_app import mensaje_error
from datos.modelos.clases_programadas import Clases_programadas
from datos.repositorios.repo_clases_programadas import (
    listado_clases_programadas,
    obtener_clase_programada,
    guardar_clase_programada,
    eliminar_clase_programada,
    verificar_disponibilidad_de_sala
)


def lista_clases_programadas(tabla: PrettyTable):
    try:
        tabla.field_names = ['ID', 'Horario', 'Fecha', 'Sala', 'Asignatura', 'Sección']
        for cp in listado_clases_programadas():
            tabla.add_row([cp.id_clases_prog, cp.horario, cp.fecha, cp.sala, cp.id_asignatura.nombre, cp.id_seccion.numero])
        return tabla
    except Exception as error:
        print(f'{mensaje_error}{error}')


def obtener_objeto_clase_programada(id_clases_prog: int):
    try:
        return obtener_clase_programada(id_clases_prog)
    except Exception as error:
        print(f'{mensaje_error}{error}')
        return None


def crear_objeto_clase_programada(horario, fecha, sala, id_asignatura, id_seccion):
    try:
        nueva = Clases_programadas()
        nueva.horario = horario
        nueva.fecha = fecha
        nueva.sala = sala
        nueva.id_asignatura = id_asignatura
        nueva.id_seccion = id_seccion
        guardar_clase_programada(nueva)
    except Exception as error:
        print(f'{mensaje_error}{error}')


def eliminar_objeto_clase_programada(clase_prog: Clases_programadas):
    try:
        return eliminar_clase_programada(clase_prog)
    except Exception as error:
        print(f'{mensaje_error}{error}')
        return False


def disponibilidad_sala(sala: str) -> bool:
    try:
        return verificar_disponibilidad_de_sala(sala)
    except Exception as error:
        print(f'{mensaje_error}{error}')
        return False
