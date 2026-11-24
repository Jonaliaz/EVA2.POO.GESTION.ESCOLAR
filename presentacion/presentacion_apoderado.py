from prettytable import PrettyTable
from auxiliares import (
    mensaje_error,
    validar_largo_string,
    validar_correo,
    validar_numero
)
from negocio.negocio_apoderado import (
    lista_apoderados,
    obtener_objeto_apoderado,
    crear_objeto_apoderado,
    actualizar_objeto_apoderado
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


def _pedir_correo(mensaje: str, largo: int = 50, opcional: bool = False) -> str:
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


def _pedir_telefono(mensaje: str, largo: int = 50, opcional: bool = False) -> str:
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
        numero, msg = validar_numero(entrada)
        print(msg)
        if numero != 0 or entrada == '0':
            return str(numero)


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


def mostrar_apoderados():
    try:
        print(lista_apoderados(PrettyTable()))
    except Exception as error:
        print(f'{mensaje_error}{error}')


def agregar_apoderado():
    try:
        nombre = _pedir_texto('Ingrese nombre del apoderado: ', 40)
        correo = _pedir_correo('Ingrese correo del apoderado: ', 50)
        telefono = _pedir_telefono('Ingrese teléfono del apoderado: ', 50)
        crear_objeto_apoderado(nombre, correo, telefono)
    except Exception as error:
        print(f'{mensaje_error}{error}')


def modificar_apoderado():
    try:
        mostrar_apoderados()
        id_apoderado = _pedir_entero('Ingrese el ID del apoderado a modificar: ')
        encontrado = obtener_objeto_apoderado(id_apoderado)
        if encontrado:
            print(f'\nApoderado encontrado: {encontrado.nombre}')
            nombre = _pedir_texto_opcional('Nuevo nombre (o ENTER para conservar): ', 40)
            correo = _pedir_correo('Nuevo correo (o ENTER para conservar): ', 50, opcional=True)
            telefono = _pedir_telefono('Nuevo teléfono (o ENTER para conservar): ', 50, opcional=True)
            actualizar_objeto_apoderado(nombre, correo, telefono, encontrado)
        else:
            print('Apoderado no encontrado.')
    except Exception as error:
        print(f'{mensaje_error}{error}')
