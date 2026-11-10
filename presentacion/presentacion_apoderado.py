from prettytable import PrettyTable
from auxiliares import mensaje_error
from negocio.negocio_apoderado import (
    lista_apoderados,
    crear_objeto_apoderado
)


def _pedir_texto(mensaje: str) -> str:
    valor = ''
    while valor == '':
        valor = input(mensaje).strip()
        if valor == '':
            print("El campo no puede estar vacío.")
    return valor


def mostrar_apoderados():
    print(lista_apoderados(PrettyTable()))


def agregar_apoderado():
    nombre = _pedir_texto('Ingrese nombre del apoderado: ')
    correo = _pedir_texto('Ingrese correo del apoderado: ')
    telefono = _pedir_texto('Ingrese teléfono del apoderado: ')
    crear_objeto_apoderado(nombre, correo, telefono)
