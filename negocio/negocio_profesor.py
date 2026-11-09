from prettytable import PrettyTable
from auxiliares.info_app import mensaje_error
from datos.modelos.profesor import Profesor
from datos.modelos.asignatura import Asignatura
from datos.repositorios.repo_profesor import (
    listado_profesores,
    obtener_profesor,
    guardar_profesor,
    eliminar_profesor,
    asignar_asignatura
)


def lista_profesores(tabla: PrettyTable):
    try:
        tabla.field_names = ['ID', 'Nombre', 'Correo', 'Teléfono']
        for p in listado_profesores():
            tabla.add_row([p.id_profesor, p.nombre, p.correo, p.telefono])
        return tabla
    except Exception as error:
        print(f'{mensaje_error}{error}')


def obtener_objeto_profesor(id_profesor: int):
    try:
        return obtener_profesor(id_profesor)
    except Exception as error:
        print(f'{mensaje_error}{error}')
        return None


def crear_objeto_profesor(nombre, correo, telefono):
    try:
        nuevo = Profesor()
        nuevo.nombre = nombre
        nuevo.correo = correo
        nuevo.telefono = telefono
        guardar_profesor(nuevo)
    except Exception as error:
        print(f'{mensaje_error}{error}')


def actualizar_objeto_profesor(nombre, correo, telefono, profesor: Profesor):
    try:
        if nombre != '':
            profesor.nombre = nombre
        if correo != '':
            profesor.correo = correo
        if telefono != '':
            profesor.telefono = telefono
        guardar_profesor(profesor)
    except Exception as error:
        print(f'{mensaje_error}{error}')


def eliminar_objeto_profesor(profesor: Profesor):
    try:
        return eliminar_profesor(profesor)
    except Exception as error:
        print(f'{mensaje_error}{error}')
        return False


def asignar_asignatura_profesor(profesor: Profesor, asignatura: Asignatura):
    try:
        return asignar_asignatura(profesor, asignatura)
    except Exception as error:
        print(f'{mensaje_error}{error}')
        return False
