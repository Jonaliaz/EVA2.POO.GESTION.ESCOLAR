from prettytable import PrettyTable
from auxiliares.info_app import mensaje_error
from datos.modelos.usuario import Usuarios
from datos.repositorios.repo_usuario import (
    listado_usuarios,
    listado_usuarios_habil,
    listado_usuarios_deshabilitados,
    obtener_usuario,
    guardar_usuario,
    eliminar_usuario
)


def lista_usuarios(tabla: PrettyTable):
    try:
        tabla.field_names = ['ID', 'Nombre', 'Apellido', 'Correo', 'RUT', 'Habilitado']
        for u in listado_usuarios():
            estado = 'Sí' if u.habilitado == 1 else 'No'
            tabla.add_row([u.id_usuario, u.nombre, u.apellido, u.correo, u.rut, estado])
        return tabla
    except Exception as error:
        print(f'{mensaje_error}{error}')


def lista_usuarios_habilitados(tabla: PrettyTable):
    try:
        tabla.field_names = ['ID', 'Nombre', 'Apellido', 'Correo', 'RUT']
        for u in listado_usuarios_habil():
            tabla.add_row([u.id_usuario, u.nombre, u.apellido, u.correo, u.rut])
        return tabla
    except Exception as error:
        print(f'{mensaje_error}{error}')


def lista_usuarios_inactivos(tabla: PrettyTable):
    try:
        tabla.field_names = ['ID', 'Nombre', 'Apellido', 'Correo', 'RUT']
        for u in listado_usuarios_deshabilitados():
            tabla.add_row([u.id_usuario, u.nombre, u.apellido, u.correo, u.rut])
        return tabla
    except Exception as error:
        print(f'{mensaje_error}{error}')


def obtener_objeto_usuario(id_usuario: int):
    try:
        return obtener_usuario(id_usuario)
    except Exception as error:
        print(f'{mensaje_error}{error}')
        return None


def crear_objeto_usuario(nombre, apellido, correo, rut):
    try:
        nuevo = Usuarios()
        nuevo.nombre = nombre
        nuevo.apellido = apellido
        nuevo.correo = correo
        nuevo.rut = rut
        guardar_usuario(nuevo)
    except Exception as error:
        print(f'{mensaje_error}{error}')


def actualizar_objeto_usuario(nombre, apellido, correo, rut, habilitado, usuario: Usuarios):
    try:
        if nombre != '':
            usuario.nombre = nombre
        if apellido != '':
            usuario.apellido = apellido
        if correo != '':
            usuario.correo = correo
        if rut != '':
            usuario.rut = rut
        if habilitado != '':
            usuario.habilitado = int(habilitado)
        guardar_usuario(usuario)
    except Exception as error:
        print(f'{mensaje_error}{error}')


def eliminar_objeto_usuario(usuario: Usuarios):
    try:
        return eliminar_usuario(usuario)
    except Exception as error:
        print(f'{mensaje_error}{error}')
        return False
