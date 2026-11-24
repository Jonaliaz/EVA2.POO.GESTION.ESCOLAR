from prettytable import PrettyTable
from auxiliares import (
    mensaje_error,
    validar_largo_string,
    validar_correo,
    validar_numero
)
from negocio.negocio_profesor import (
    lista_profesores,
    obtener_objeto_profesor,
    crear_objeto_profesor,
    actualizar_objeto_profesor,
    eliminar_objeto_profesor
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


def _pedir_correo(mensaje: str, largo: int = 60, opcional: bool = False) -> str:
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


def _pedir_telefono(mensaje: str, largo: int = 18, opcional: bool = False) -> str:
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


def mostrar_profesores():
    try:
        print(lista_profesores(PrettyTable()))
    except Exception as error:
        print(f'{mensaje_error}{error}')


def agregar_profesor():
    try:
        nombre = _pedir_texto('Ingrese nombre del profesor: ', 50)
        correo = _pedir_correo('Ingrese correo del profesor: ', 60)
        telefono = _pedir_telefono('Ingrese teléfono del profesor: ', 18)
        crear_objeto_profesor(nombre, correo, telefono)
    except Exception as error:
        print(f'{mensaje_error}{error}')


def modificar_profesor():
    try:
        mostrar_profesores()
        id_profesor = _pedir_entero('Ingrese el ID del profesor a modificar: ')
        encontrado = obtener_objeto_profesor(id_profesor)
        if encontrado:
            print(f'\nProfesor encontrado: {encontrado.nombre}')
            nombre = _pedir_texto_opcional('Nuevo nombre (o ENTER para conservar): ', 50)
            correo = _pedir_correo('Nuevo correo (o ENTER para conservar): ', 60, opcional=True)
            telefono = _pedir_telefono('Nuevo teléfono (o ENTER para conservar): ', 18, opcional=True)
            actualizar_objeto_profesor(nombre, correo, telefono, encontrado)
        else:
            print('Profesor no encontrado.')
    except Exception as error:
        print(f'{mensaje_error}{error}')


def borrar_profesor():
    try:
        mostrar_profesores()
        id_profesor = _pedir_entero('Ingrese el ID del profesor a eliminar: ')
        encontrado = obtener_objeto_profesor(id_profesor)
        if encontrado:
            eliminar_objeto_profesor(encontrado)
        else:
            print('Profesor no encontrado.')
    except Exception as error:
        print(f'{mensaje_error}{error}')
