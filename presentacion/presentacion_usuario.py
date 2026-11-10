from prettytable import PrettyTable
from auxiliares import mensaje_error
from negocio.negocio_usuarios import (
    lista_usuarios,
    lista_usuarios_habilitados,
    lista_usuarios_inactivos,
    obtener_objeto_usuario,
    crear_objeto_usuario,
    actualizar_objeto_usuario,
    eliminar_objeto_usuario
)


def _pedir_texto(mensaje: str) -> str:
    valor = ''
    while valor == '':
        valor = input(mensaje).strip()
        if valor == '':
            print("El campo no puede estar vacío.")
    return valor


def _pedir_entero(mensaje: str) -> int:
    while True:
        try:
            return int(input(mensaje).strip())
        except ValueError:
            print("Entrada inválida: debe ingresar un número entero.")


def mostrar_usuarios():
    try:
        print(lista_usuarios(PrettyTable()))
    except Exception as error:
        print(f'{mensaje_error}{error}')


def mostrar_usuarios_habilitados():
    try:
        print(lista_usuarios_habilitados(PrettyTable()))
    except Exception as error:
        print(f'{mensaje_error}{error}')


def mostrar_usuarios_deshabilitados():
    try:
        print(lista_usuarios_inactivos(PrettyTable()))
    except Exception as error:
        print(f'{mensaje_error}{error}')


def agregar_usuario():
    try:
        nombre = _pedir_texto('Ingrese nombre del usuario: ')
        apellido = _pedir_texto('Ingrese apellido del usuario: ')
        correo = _pedir_texto('Ingrese correo del usuario: ')
        rut = _pedir_texto('Ingrese RUT del usuario: ')
        crear_objeto_usuario(nombre, apellido, correo, rut)
    except Exception as error:
        print(f'{mensaje_error}{error}')


def modificar_usuario():
    try:
        mostrar_usuarios()
        id_usuario = _pedir_entero('Ingrese el ID del usuario a modificar: ')
        encontrado = obtener_objeto_usuario(id_usuario)
        if encontrado:
            print(f'\nUsuario encontrado: {encontrado.nombre} {encontrado.apellido or ""}'.strip())
            nombre = input('Nuevo nombre (o ENTER para conservar): ').strip()
            apellido = input('Nuevo apellido (o ENTER para conservar): ').strip()
            correo = input('Nuevo correo (o ENTER para conservar): ').strip()
            rut = input('Nuevo RUT (o ENTER para conservar): ').strip()
            habilitado = input('Estado habilitado (1 = Sí, 0 = No, o ENTER para conservar): ').strip()
            actualizar_objeto_usuario(nombre, apellido, correo, rut, habilitado, encontrado)
        else:
            print('Usuario no encontrado.')
    except Exception as error:
        print(f'{mensaje_error}{error}')


def borrar_usuario():
    try:
        mostrar_usuarios()
        id_usuario = _pedir_entero('Ingrese el ID del usuario a eliminar: ')
        encontrado = obtener_objeto_usuario(id_usuario)
        if encontrado:
            eliminar_objeto_usuario(encontrado)
        else:
            print('Usuario no encontrado.')
    except Exception as error:
        print(f'{mensaje_error}{error}')
