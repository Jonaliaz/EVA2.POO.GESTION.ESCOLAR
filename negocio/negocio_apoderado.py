from prettytable import PrettyTable
from auxiliares.info_app import mensaje_error
from datos.modelos.apoderado import Apoderado
from datos.repositorios.repo_apoderado import (
    listado_apoderados,
    obtener_apoderado,
    guardar_apoderado,
    eliminar_apoderado
)


def lista_apoderados(tabla: PrettyTable):
    try:
        tabla.field_names = ['ID', 'Nombre', 'Correo', 'Teléfono']
        for ap in listado_apoderados():
            tabla.add_row([ap.id_apoderado, ap.nombre, ap.correo, ap.telefono])
        return tabla
    except Exception as error:
        print(f'{mensaje_error}{error}')


def obtener_objeto_apoderado(id_apoderado: int):
    try:
        return obtener_apoderado(id_apoderado)
    except Exception as error:
        print(f'{mensaje_error}{error}')
        return None


def crear_objeto_apoderado(nombre, correo, telefono):
    try:
        nuevo = Apoderado()
        nuevo.nombre = nombre
        nuevo.correo = correo
        nuevo.telefono = telefono
        guardar_apoderado(nuevo)
    except Exception as error:
        print(f'{mensaje_error}{error}')


def actualizar_objeto_apoderado(nombre, correo, telefono, apoderado: Apoderado):
    try:
        if nombre != '':
            apoderado.nombre = nombre
        if correo != '':
            apoderado.correo = correo
        if telefono != '':
            apoderado.telefono = telefono
        guardar_apoderado(apoderado)
    except Exception as error:
        print(f'{mensaje_error}{error}')


def eliminar_objeto_apoderado(apoderado: Apoderado):
    try:
        return eliminar_apoderado(apoderado)
    except Exception as error:
        print(f'{mensaje_error}{error}')
        return False
