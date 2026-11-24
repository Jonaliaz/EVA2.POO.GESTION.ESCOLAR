from prettytable import PrettyTable
from auxiliares import (
    mensaje_error,
    validar_rut,
    validar_largo_string,
    validar_correo,
    validar_numero
)
from negocio.negocio_usuarios import (
    lista_usuarios,
    lista_usuarios_habilitados,
    lista_usuarios_inactivos,
    obtener_objeto_usuario,
    crear_objeto_usuario,
    actualizar_objeto_usuario,
    eliminar_objeto_usuario
)


def _pedir_texto(mensaje: str, largo: int = 0) -> str:
    valor = ''
    while valor == '':
        valor = input(mensaje).strip()
        if valor == '':
            print("El campo no puede estar vacío.")
        elif largo > 0:
            valor, msg = validar_largo_string(valor, largo)
            if valor == '':
                print(msg)
    return valor


def _pedir_texto_opcional(mensaje: str, largo: int = 0) -> str:
    while True:
        valor = input(mensaje).strip()
        if valor == '':
            return ''
        if largo > 0:
            val_validado, msg = validar_largo_string(valor, largo)
            if val_validado == '':
                print(msg)
                continue
        return valor


def _pedir_correo(mensaje: str, largo: int = 100, opcional: bool = False) -> str:
    while True:
        entrada = input(mensaje).strip()
        if entrada == '':
            if opcional:
                return ''
            print("El campo no puede estar vacío.")
            continue
        if largo > 0:
            val_largo, msg_largo = validar_largo_string(entrada, largo)
            if val_largo == '':
                print(msg_largo)
                continue
        correo, msg = validar_correo(entrada)
        print(msg)
        if correo != '':
            return correo


def _pedir_rut(mensaje: str, largo: int = 12, opcional: bool = False) -> str:
    while True:
        entrada = input(mensaje).strip()
        if entrada == '':
            if opcional:
                return ''
            print("El campo no puede estar vacío.")
            continue
        if largo > 0:
            val_largo, msg_largo = validar_largo_string(entrada, largo)
            if val_largo == '':
                print(msg_largo)
                continue
        rut, msg = validar_rut(entrada)
        print(msg)
        if rut != '':
            return rut


def _pedir_entero(mensaje: str) -> int:
    while True:
        entrada = input(mensaje).strip()
        if entrada == '':
            print("El campo no puede estar vacío.")
            continue
        numero, msg = validar_numero(entrada)
        if numero == 0 and entrada != '0':
            print(msg)
        else:
            return numero


def _pedir_habilitado_opcional(mensaje: str) -> str:
    while True:
        entrada = input(mensaje).strip()
        if entrada == '':
            return ''
        numero, msg = validar_numero(entrada)
        if (numero == 0 and entrada != '0') or numero not in (0, 1):
            print("Entrada inválida: debe ingresar 1 (Sí), 0 (No) o presionar ENTER para conservar.")
        else:
            return str(numero)


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
        nombre = _pedir_texto('Ingrese nombre del usuario: ', 25)
        apellido = _pedir_texto('Ingrese apellido del usuario: ', 25)
        correo = _pedir_correo('Ingrese correo del usuario: ', 100)
        rut = _pedir_rut('Ingrese RUT del usuario: ', 12)
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
            nombre = _pedir_texto_opcional('Nuevo nombre (o ENTER para conservar): ', 25)
            apellido = _pedir_texto_opcional('Nuevo apellido (o ENTER para conservar): ', 25)
            correo = _pedir_correo('Nuevo correo (o ENTER para conservar): ', 100, opcional=True)
            rut = _pedir_rut('Nuevo RUT (o ENTER para conservar): ', 12, opcional=True)
            habilitado = _pedir_habilitado_opcional('Estado habilitado (1 = Sí, 0 = No, o ENTER para conservar): ')
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
