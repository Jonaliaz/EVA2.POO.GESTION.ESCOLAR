import bcrypt
from prettytable import PrettyTable
from auxiliares.info_app import mensaje_error
from datos.modelos.usuario import Usuarios
from datos.repositorios.repo_usuario import (
    listado_usuarios,
    listado_usuarios_habil,
    listado_usuarios_deshabilitados,
    obtener_usuario,
    obtener_usuario_correo,
    obtener_usuario_rut,
    obtener_usuario_correo_o_rut,
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


def obtener_usuario_por_correo(correo: str):
    try:
        return obtener_usuario_correo(correo)
    except Exception as error:
        print(f'{mensaje_error}{error}')
        return None


def obtener_usuario_por_rut(rut: str):
    try:
        return obtener_usuario_rut(rut)
    except Exception as error:
        print(f'{mensaje_error}{error}')
        return None


def obtener_usuario_login(identificador: str):
    try:
        return obtener_usuario_correo_o_rut(identificador)
    except Exception as error:
        print(f'{mensaje_error}{error}')
        return None


def encriptar_contrasena(contrasena: str) -> str:
    if not contrasena:
        return ''
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(contrasena.encode('utf-8'), salt)
    return hashed.decode('utf-8')


def verificar_contrasena(contrasena_plana: str, contrasena_hash: str) -> bool:
    try:
        if not contrasena_plana or not contrasena_hash:
            return False
        if contrasena_hash.startswith('$2b$') or contrasena_hash.startswith('$2a$'):
            return bcrypt.checkpw(
                contrasena_plana.encode('utf-8'),
                contrasena_hash.encode('utf-8')
            )
        return contrasena_plana == contrasena_hash
    except Exception as error:
        print(f'{mensaje_error}{error}')
        return False


def crear_objeto_usuario(nombre, apellido, correo, rut, contrasena=''):
    try:
        nuevo = Usuarios()
        nuevo.nombre = nombre
        nuevo.apellido = apellido
        nuevo.correo = correo
        nuevo.rut = rut
        nuevo.contrasena = encriptar_contrasena(contrasena) if contrasena else ''
        guardar_usuario(nuevo)
    except Exception as error:
        print(f'{mensaje_error}{error}')


def actualizar_objeto_usuario(nombre, apellido, correo, rut, habilitado, usuario: Usuarios, contrasena=''):
    try:
        if nombre != '':
            usuario.nombre = nombre
        if apellido != '':
            usuario.apellido = apellido
        if correo != '':
            usuario.correo = correo
        if rut != '':
            usuario.rut = rut
        if contrasena != '':
            usuario.contrasena = encriptar_contrasena(contrasena)
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
