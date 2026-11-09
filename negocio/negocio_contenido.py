from prettytable import PrettyTable
from auxiliares.info_app import mensaje_error
from datos.modelos.contenido import Contenido
from datos.repositorios.repo_contenido import (
    listado_contenidos,
    obtener_contenido,
    guardar_contenido,
    eliminar_contenido
)


def lista_contenidos(tabla: PrettyTable):
    try:
        tabla.field_names = ['ID', 'Nombre Contenido', 'Número Unidad']
        for cont in listado_contenidos():
            tabla.add_row([cont.id_contenido, cont.nombre, cont.numero_unidad])
        return tabla
    except Exception as error:
        print(f'{mensaje_error}{error}')


def obtener_objeto_contenido(id_contenido: int):
    try:
        return obtener_contenido(id_contenido)
    except Exception as error:
        print(f'{mensaje_error}{error}')
        return None


def crear_objeto_contenido(nombre, numero_unidad):
    try:
        nuevo = Contenido()
        nuevo.nombre = nombre
        nuevo.numero_unidad = numero_unidad
        guardar_contenido(nuevo)
    except Exception as error:
        print(f'{mensaje_error}{error}')


def eliminar_objeto_contenido(contenido: Contenido):
    try:
        return eliminar_contenido(contenido)
    except Exception as error:
        print(f'{mensaje_error}{error}')
        return False
