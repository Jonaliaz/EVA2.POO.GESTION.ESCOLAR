from prettytable import PrettyTable
from auxiliares.info_app import mensaje_error
from datos.modelos.registro_academico import Registro_academico
from datos.repositorios.repo_registro_academico import (
    listado_registros_academicos,
    obtener_registro_academico,
    guardar_registro_academico,
    eliminar_registro_academico
)


def lista_registros_academicos(tabla: PrettyTable):
    try:
        tabla.field_names = ['ID', 'Fecha', 'Curso', 'Contenido']
        for reg in listado_registros_academicos():
            tabla.add_row([reg.id_registro_academico, reg.fecha, reg.id_curso.nombre, reg.id_contenido.nombre])
        return tabla
    except Exception as error:
        print(f'{mensaje_error}{error}')


def obtener_objeto_registro_academico(id_registro_academico: int):
    try:
        return obtener_registro_academico(id_registro_academico)
    except Exception as error:
        print(f'{mensaje_error}{error}')
        return None


def crear_objeto_registro_academico(fecha, id_curso, id_contenido):
    try:
        nuevo = Registro_academico()
        nuevo.fecha = fecha
        nuevo.id_curso = id_curso
        nuevo.id_contenido = id_contenido
        guardar_registro_academico(nuevo)
    except Exception as error:
        print(f'{mensaje_error}{error}')


def eliminar_objeto_registro_academico(registro: Registro_academico):
    try:
        return eliminar_registro_academico(registro)
    except Exception as error:
        print(f'{mensaje_error}{error}')
        return False
